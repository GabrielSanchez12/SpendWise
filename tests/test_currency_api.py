from unittest.mock import Mock, patch
from spendwise.currency_api import get_exchange_rate


@patch("spendwise.currency_api.requests.get")
def test_get_exchange_rate_with_mocked_api(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        "rates": {
            "USD": 0.18,
        }
    }
    mock_response.raise_for_status.return_value = None

    mock_get.return_value = mock_response

    result = get_exchange_rate("USD")

    assert result == 0.18
    mock_get.assert_called_once()