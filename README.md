# LetsVoteBot

A self-hostable Discord bot that runs **Ranked Choice Voting (RCV)** elections. Written in Python, deployable with Docker. Works locally (e.g., Synology DSM) or on cloud (e.g., Fly.io, Railway).

---

## Features

- Instant-runoff ranked choice voting
- Simple command syntax: `!rcv A,B,C | user1:1,2,3 user2:2,1,3`
- Environment variable support via `.env`
- Fast Docker build using `uv`

---

## Commands

```text
!rcv A,B,C | user1:1,2,3 user2:2,1,3 user3:3,2,1
