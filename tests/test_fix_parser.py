import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.fix_parser import parse_fix_message


def test_fix_parser():
    message = "35=D|11=ORD001|55=AAPL|54=1|38=100|44=190.50|"

    result = parse_fix_message(message)

    assert result["client_order_id"] == "ORD001"
    assert result["symbol"] == "AAPL"
