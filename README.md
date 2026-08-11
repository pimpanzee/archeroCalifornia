# archeroCalifornia

Automation for the `california` Archero 2 guild's Discord.

## Daily Discord post

`.github/workflows/discord-daily-post.yml` posts a link to the guild roster
tracker into Discord once a day (and can be triggered manually from the
Actions tab).

### Setup

1. In Discord: **Server Settings → Integrations → Webhooks → New Webhook**,
   pick the channel to post in, and copy the webhook URL.
2. In GitHub: **Settings → Secrets and variables → Actions → New repository
   secret**, name it `DISCORD_WEBHOOK_URL`, and paste the URL in as the value.
3. That's it — the workflow runs daily at 15:00 UTC. Change the `cron` line
   in the workflow file to adjust the time, or run it manually via
   **Actions → Post guild roster link to Discord → Run workflow**.
