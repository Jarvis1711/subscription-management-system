# Proof of Concept - Subscription Management System

## Deployment Readiness
- Web app + API routes active
- Container and PaaS deployment files included
- Automated test suite and CI workflow included

## Smoke Commands
```bash
python run.py
curl http://localhost:5000/api/health
curl http://localhost:5000/api/schema
curl -X POST http://localhost:5000/api/items   -H "Content-Type: application/json"   -d '{"title":"Phase3 Demo","status":"draft","payload":{"client":"sample","value_estimate":5,"commercial_notes":"notes"}}'
curl http://localhost:5000/api/metrics
```

## Metadata
- Generated UTC: 2026-03-24T16:15:12.037512+00:00
- Phase: 3
- Domain: Business
