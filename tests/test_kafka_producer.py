from unittest.mock import MagicMock, patch
from kafka.errors import KafkaError
from kafka_broker.producer import send_to_kafka, resend_failed_messages
import pytest
import os

TEST_FILE = 'failed_messages.txt'


# def test_kafka_send_success():
#     mock_producer = MagicMock()
#     mock_producer.send.return_value = MagicMock()
#     mock_producer.flush.return_value = None

#     msg = {"ID": "123", "data": "some_data"}
#     result = send_to_kafka(mock_producer, msg, retries=1, delay=0)

#     assert result is True
#     mock_producer.send.assert_called_once()

@pytest.fixture
def setup_failed_message():
    test_message = {'ID': 'TEST1', 'F': 0.25}
    with open(TEST_FILE, "w", encoding="utf-8") as f:
        f.write(str(test_message) + "\n")
    yield test_message
    os.remove(TEST_FILE)
    
@patch("kafka_broker.producer.send_to_kafka")
def test_resend_failed_messages(mock_send, setup_failed_message):
    mock_producer = MagicMock()
    resend_failed_messages(mock_producer)
    mock_send.assert_called_with(mock_producer, str(setup_failed_message))


@patch("kafka_broker.producer.send_to_kafka")
def test_resend_message_failure_handled(mock_send, setup_failed_message, capsys):
    mock_producer = MagicMock()
    mock_send.side_effect = Exception("Kafka down")

    resend_failed_messages(mock_producer)

    captured = capsys.readouterr()
    assert "Error while retrying to send failed message" in captured.out
    

# def test_resend_failed_messages(tmp_path):
#     failed_path = tmp_path / "failed_messages.txt"
#     msg = '{"ID":"METEO1","F": 0.25}'
#     failed_path.write_text(msg)

#     fake_producer = MagicMock()
#     with patch("kafka_broker.producer.open", open(failed_path, 'r')), \
#          patch("kafka_broker.producer.send_to_kafka") as mocked_send:
#         from kafka_broker.producer import resend_failed_messages
#         resend_failed_messages(fake_producer)
#         mocked_send.assert_called_once()