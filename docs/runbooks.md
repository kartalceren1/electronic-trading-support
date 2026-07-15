# Electronic Trading Support Runbooks


# 1. Exchange Connectivity Reset

## Symptoms

- Orders remain pending
- No execution reports received
- FIX session disconnected

## Investigation

1. Check application logs
2. Search by ClOrdID or OrderID
3. Verify FIX connection status
4. Check exchange heartbeat messages

## Resolution

- Restart FIX session
- Confirm connection recovery
- Resubmit failed orders if required

## Root Cause Examples

- Network interruption
- Exchange session timeout
- Invalid connection configuration



# 2. Rejected Order

## Symptoms

- Order status shows REJECTED
- Exchange sends rejection execution report

## Investigation

1. Search order using ClOrdID
2. Check FIX reject message
3. Validate symbol, quantity and price

## Resolution

- Correct invalid order parameters
- Resubmit order if approved

## Root Cause Examples

- Invalid symbol
- Incorrect quantity
- Trading restriction



# 3. Missing Execution Report

## Symptoms

- Order accepted but no fill received
- Order remains pending

## Investigation

1. Search order ID
2. Check execution report logs
3. Compare sent orders with received executions

## Resolution

- Request execution status from exchange
- Replay missing execution message

## Root Cause Examples

- Message delay
- Dropped FIX message
- Exchange processing issue



# 4. Stale Market Data

## Symptoms

- Prices stop updating
- Orders use outdated prices

## Investigation

1. Check market data timestamps
2. Verify feed connection
3. Review market data logs

## Resolution

- Restart market data feed
- Confirm new timestamps

## Root Cause Examples

- Feed interruption
- Network latency



# 5. System Outage

## Symptoms

- Dashboard unavailable
- Orders cannot be processed

## Investigation

1. Check application container
2. Check database connection
3. Review system logs

## Resolution

- Restart failed services
- Verify database availability
- Confirm order processing recovery