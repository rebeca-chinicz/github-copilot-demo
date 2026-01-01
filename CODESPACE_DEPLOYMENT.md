# OctoFit Tracker - Codespace Deployment Guide

## Quick Start for Codespace

When deploying to GitHub Codespaces, follow these steps to configure the frontend API endpoints:

### Step 1: Get Your Codespace Name
Your codespace URL will be in the format:
```
https://[CODESPACE-NAME]-8001.app.github.dev
```

The codespace name appears in:
- VS Code: Bottom left corner
- Browser URL: `github.com/codespaces/[CODESPACE-NAME]`

### Step 2: Update config.js

Edit `octofit-tracker/frontend/src/config.js`:

**BEFORE (Local Development):**
```javascript
const API_BASE_URL = 'http://localhost:8001';
```

**AFTER (Codespace):**
```javascript
const API_BASE_URL = 'https://[YOUR-CODESPACE-NAME]-8001.app.github.dev';
```

Example with actual codespace name:
```javascript
const API_BASE_URL = 'https://congenial-robot-xyz123-8001.app.github.dev';
```

### Step 3: Restart React Server
After updating config.js, restart the React development server:
```bash
# Stop the current server (Ctrl+C)
# Then restart:
cd octofit-tracker/frontend
npm start
```

### Step 4: Access the App
- **React App**: `https://[CODESPACE-NAME]-3000.app.github.dev`
- **Django API**: `https://[CODESPACE-NAME]-8001.app.github.dev/api/`

## Environment Variable Method (Optional)

For better practice, you can use environment variables:

1. Create `.env` file in `octofit-tracker/frontend/`:
```
REACT_APP_API_URL=https://[CODESPACE-NAME]-8001.app.github.dev
```

2. Update `config.js`:
```javascript
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8001';
export default API_BASE_URL;
```

## Port Configuration

- **Frontend (React)**: Port 3000
- **Backend (Django)**: Port 8001
- **MongoDB**: Port 27017 (internal only)

Make sure Django is running on port 8001:
```bash
python manage.py runserver 0.0.0.0:8001
```

## Troubleshooting

### Issue: "Failed to fetch" errors
**Solution**: Check that:
1. Django server is running on 0.0.0.0:8001
2. Codespace URL in config.js is correct
3. CORS is enabled in Django settings (it is by default)

### Issue: Mixed content (http/https) errors
**Solution**: 
- Always use `https://` for codespace URLs
- Always use `http://` for localhost

### Issue: Cannot connect to API
**Check**:
```bash
# SSH into backend terminal
cd octofit-tracker/backend
python manage.py runserver 0.0.0.0:8001
```

Verify the server responds:
```bash
curl https://[CODESPACE-NAME]-8001.app.github.dev/api/
```

## All API Endpoints

After configuration, the following endpoints will be available:

```
GET    https://[CODESPACE-NAME]-8001.app.github.dev/api/users/
GET    https://[CODESPACE-NAME]-8001.app.github.dev/api/teams/
GET    https://[CODESPACE-NAME]-8001.app.github.dev/api/activities/
GET    https://[CODESPACE-NAME]-8001.app.github.dev/api/leaderboard/
GET    https://[CODESPACE-NAME]-8001.app.github.dev/api/workouts/
```

## Summary

✅ All components are pre-configured with `config.js` for easy switching
✅ Local development uses `http://localhost:8001`
✅ Codespace deployment uses `https://[NAME]-8001.app.github.dev`
✅ Single file change needed: `src/config.js`

That's it! The frontend is production-ready for deployment.
