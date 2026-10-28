# Security

Report vulnerabilities privately to Farshad Farshidfar at
[farshidfar@gmail.com](mailto:farshidfar@gmail.com), or use this repository's
private vulnerability reporting feature when available. Do not post credentials,
confidential notebooks, or exploit details in a public issue.

Include affected versions, a minimal synthetic reproduction, and the expected
security boundary. Reports are handled by a volunteer maintainer; no response
time or service-level guarantee is promised.

The current maintained release line is 0.1.x for the host ranges in the README.
Older previews should be upgraded before reporting an issue. Jupyter server,
kernel, authentication, and dependency vulnerabilities belong to their respective
projects unless Neat changes the affected behavior.

Neat has no external service, telemetry, or server extension. Its unauthenticated
browser-test configuration is restricted to isolated loopback tests and must
never be used in production. Registry publishing is manual, environment-approved,
and uses short-lived Trusted Publishing credentials.
