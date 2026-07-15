# Electronic Trading Support Simulator

A Python-based trading support simulator built to replicate common issues faced by electronic trading support teams.

The project simulates a simplified electronic trading environment where FIX order messages are processed, order states are tracked, incidents are detected, and support engineers can investigate issues through a Flask dashboard.

The purpose of this project was to build something similar to the internal tools and workflows used by application support engineers working with trading systems.

---

# Project Overview

Electronic trading systems process large numbers of orders between traders, applications, and exchanges. When problems occur, support teams need to quickly identify the cause of issues such as:

- Rejected orders
- Missing execution reports
- Exchange connectivity failures
- System outages
- Invalid trading messages

This project recreates these scenarios using sample FIX messages, PostgreSQL storage, automated incident classification, and a monitoring dashboard.

---

# Features

## FIX Message Parser

The application processes simplified FIX order and execution messages.

The parser extracts important trading fields including:

- ClOrdID
- OrderID
- Symbol
- Quantity
- Price
- Order status

Supported scenarios:

- New order messages
- Execution reports
- Rejected orders
- Missing execution reports
- Malformed FIX messages

---

## Order Management

Orders are stored in PostgreSQL and tracked through their lifecycle.

Supported order states:

- PENDING
- FILLED
- REJECTED

The system can identify orders that require investigation, including:

- Orders rejected by the exchange
- Orders with missing execution reports
- Orders stuck in pending states

---

## Incident Detection

The simulator creates incidents based on common trading support problems.

Example incidents:

| Incident | Description | Severity |
| --- | --- | --- |
| Order Rejection | Exchange rejected an order | Medium |
| Missing Execution | Execution report not received | High |
| Connectivity Issue | FIX connection failure | High |
| System Outage | Application or database unavailable | Critical |

---

## Flask Support Dashboard

The project includes a Flask dashboard that allows support engineers to view:

- Order information
- Current order status
- Incident records
- Incident severity

The dashboard represents a simplified internal monitoring tool used by support teams.

---

## Log Investigation

The project includes support-style investigation functionality.

Engineers can:

- Trace orders using ClOrdID
- Trace orders using OrderID
- Identify malformed FIX messages
- Review incident information
- Produce root cause summaries for support handover

---

# Technology Stack

| Technology | Purpose |
| --- | --- |
| Python | Application logic and FIX parsing |
| PostgreSQL | Order and incident database |
| Flask | Dashboard interface |
| Docker | Containerised application environment |
| Pytest | Automated testing |
| GitHub Actions | Continuous integration |
| Linux CLI | Support investigation workflows |

---

# Project Structure

```
electronic-trading-support/

├── app/
│   ├── dashboard.py        # Flask dashboard
│   ├── database.py         # PostgreSQL connection
│   └── fix_parser.py       # FIX message parser
│
├── tests/
│   └── test_fix_parser.py  # Automated tests
│
├── templates/
│   └── dashboard.html      # Dashboard frontend
│
├── sql/
│   └── init.sql            # Database setup and sample data
│
├── docs/
│   └── runbooks.md         # Support procedures
│
├── .github/
│   └── workflows/
│       └── tests.yml       # GitHub Actions workflow
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# Running the Application

## Requirements

Install:

- Python 3.11+
- Docker Desktop
- Git

---

## Running with Docker

Clone the repository:

```bash
git clone <repository-url>
```

Navigate into the project:

```bash
cd electronic-trading-support
```

Build the Docker containers:

```bash
docker compose build
```

Start the application:

```bash
docker compose up
```

The dashboard will be available at:

```
http://127.0.0.1:5000
```

---

# Running Tests

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Run the test suite:

```bash
pytest
```

Tests currently validate:

- FIX message parsing
- Application functionality
- Data processing logic

---

# Docker Architecture

The application runs using two Docker containers:

```
                 Browser
                    |
                    |
                    v
          Flask Dashboard Container
                    |
                    |
                    v
          PostgreSQL Database Container
```

Docker provides a consistent environment containing:

- Application dependencies
- Python runtime
- Database service
- Configuration

---

# Example Support Scenarios

## Missing Execution Report

### Problem

An order has been accepted but no execution report has been received from the exchange.

### Investigation

1. Search for the order using ClOrdID
2. Review FIX messages
3. Compare sent orders against received executions
4. Identify where processing stopped

### Possible Causes

- Exchange delay
- Dropped FIX message
- Connectivity problem
- Processing failure

---

## Rejected Order

### Problem

An order is rejected by the exchange.

### Investigation

1. Locate the order
2. Review the rejection message
3. Identify the rejection reason

### Possible Causes

- Invalid symbol
- Incorrect quantity
- Invalid order parameters
- Trading restriction

---

## Exchange Connectivity Failure

### Problem

The FIX session disconnects during trading.

### Investigation

1. Review application logs
2. Check FIX connection status
3. Verify exchange communication
4. Check heartbeat messages

### Resolution

Possible actions:

- Restart FIX session
- Restore connectivity
- Monitor message recovery

---

## System Outage

### Problem

The trading support application becomes unavailable.

### Investigation

1. Check application status
2. Check database connectivity
3. Review logs
4. Identify failed components

### Resolution

- Restart failed services
- Restore database connection
- Verify system recovery

---

# GitHub Actions CI Pipeline

The project uses GitHub Actions to automatically run tests when changes are pushed.

Workflow:

```
Developer makes change

        |

        v

Git Push

        |

        v

GitHub Actions starts

        |

        v

Install dependencies

        |

        v

Run Pytest

        |

        v

Pass / Fail Result
```

This helps ensure new changes do not break existing functionality.

---

# Support Runbooks

Support procedures are documented in:

```
docs/runbooks.md
```

The runbooks cover:

- Exchange connectivity resets
- Rejected orders
- Missing execution reports
- Stale market data
- System outages

Each runbook contains:

- Symptoms
- Investigation steps
- Resolution steps
- Possible root causes

---

# Skills Demonstrated

This project demonstrates practical skills relevant to electronic trading support roles:

- FIX protocol understanding
- Trading order lifecycle management
- Incident investigation
- Database troubleshooting
- Python development
- Log analysis
- Docker containerisation
- Automated testing
- CI/CD workflows
- Operational documentation

---

# Future Improvements

Possible future improvements:

- More complete FIX protocol support
- Real-time market data simulation
- Alert notifications
- Advanced log search
- User authentication
- More detailed trading metrics
- Production deployment using Kubernetes

---

# Why I Built This

I built this project to gain practical experience with the type of problems handled by electronic trading support teams.

The project focuses on investigating failed orders, analysing FIX messages, troubleshooting connectivity issues, and creating tools that improve operational visibility and incident response.