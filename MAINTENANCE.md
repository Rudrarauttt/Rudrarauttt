# Profile visuals

`README.md` is the public profile. Static illustrations and skill badges live in `assets/` and have no external image-service dependency. The header's CSS animations respect reduced-motion preferences.

The **Refresh profile visuals** workflow runs every day at 01:23 UTC (06:53 IST), on a manual dispatch, and when its source changes on `main`. GitHub may delay scheduled runs. The workflow publishes light and dark contribution snakes and public activity cards to the `output` branch. It uses the automatic repository token; no personal access token or paid service is needed.

The activity script reads only public, non-fork, non-archived repositories. The profile repository is excluded from the activity panel. Language percentages represent source-code bytes, not proficiency. Failed generation stops publication so the last working visuals remain available.

To refresh now, open **Actions → Refresh profile visuals → Run workflow**. To edit featured projects or skills, update the README and local SVGs. The contribution snake is an animated replay, not a keyboard-controlled game. It does not replace GitHub's native contribution calendar.

## Local generation

Run `python3 scripts/build_activity.py` from this repository. An optional `GITHUB_TOKEN` increases the public API rate limit. Set `PROFILE_USER` when adapting the script for another account.

## Dependencies

- [actions/checkout](https://github.com/actions/checkout), pinned to v7.0.1's commit.
- [Platane/snk](https://github.com/Platane/snk), pinned to the v3 commit used for the initial build.
- Python's standard library for the public activity cards.

Generated assets are isolated on `output`; the publish step appends commits without force pushing or changing `main`.
