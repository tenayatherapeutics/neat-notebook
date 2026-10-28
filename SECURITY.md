# Security

Report vulnerabilities privately to Farshad Farshidfar at
[farshidfar@gmail.com](mailto:farshidfar@gmail.com), or use
[GitHub private vulnerability reporting](https://github.com/tenayatherapeutics/neat-notebook/security/advisories/new).
Do not post credentials,
confidential notebooks, or exploit details in a public issue.

Include affected versions, a minimal synthetic reproduction, and the expected
security boundary.

The current maintained release line is 0.1.x for the host ranges in the README.
Upgrade to the latest published release before reporting an issue. Jupyter server,
kernel, authentication, and dependency vulnerabilities belong to their respective
projects unless Neat changes the affected behavior.

Neat has no external service, telemetry, or server extension. Its unauthenticated
browser-test configuration is restricted to isolated loopback tests and must
never be used in production. Registry publishing is manual, environment-approved,
and uses short-lived Trusted Publishing credentials.
