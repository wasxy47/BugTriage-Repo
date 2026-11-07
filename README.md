# BugTriage and Reproducer Room

A multi-agent bug fixing workflow that lives inside team chat. Drop a bug report into a Mattermost channel, and three specialized AI agents take it from report to verified fix — with a human approval gate before any code is changed.

Built with Switch for the Flip the Switch Hackathon (WeMakeDevs x Switch), Track 2: Best Personal or Creative Workflow.

## How it works

1. triage-agent reads the bug report (and any error log or traceback), names the faulty file and function, explains the root cause, and states the expected behavior. It never edits code.
2. repro-agent saves the buggy code and writes a real pytest test suite in its own workspace, runs it, and posts the exact failing output. It never fixes code.
3. fixer-agent proposes the exact fix and then STOPS. No file is created or edited until the human approves. After approval it applies the fix, re-runs the same test suite, saves a written case report, and ends with the line FIX VERIFIED.

The human stays in control the whole time: agents act only when tagged, and the fix only happens after an explicit approval in the channel.

## The two demo cases (both run live in the channel)

Case 002 — wrong-result logic bug (case-002 folder)
apply_discount(200, 10) returned 20.0 instead of 180.0, because the function returned the discount amount instead of the final price. A 5-test pytest suite went from 0 passed / 5 failed to 5 passed after a one-line fix.

Case 003 — crash bug (case-003 folder)
Reported like a real GitHub issue, traceback included: average_item_price([]) crashed with ZeroDivisionError when a cart was empty. A 4-test suite went from 3 passed / 1 failed to 4 passed after adding an empty-list guard.

Each case folder holds the buggy code, the test suite, the fixed code, and the case report the fixer-agent saved.

## How Switch is used

- The three agents are OpenCode agents running on a local Switch server, connected to a Mattermost channel through Switch, where each agent appears as its own bot account.
- Each agent works in its own workspace folder. There is no shared folder, so agents pass file contents to each other through the chat — every step, every file, and every test output is visible in the channel, which makes the whole workflow auditable.
- The exact instructions given to each agent are in the agents folder, so the setup can be recreated.

## Run the tests yourself

Inside either case folder, with the buggy file present the suite fails; swap in the fixed file and it passes:

python -m pytest -v

## Recreate the room

1. Install Switch Console and start a local Switch server with the bundled Mattermost.
2. Create three OpenCode agents using the instruction files in the agents folder.
3. Create a Mattermost channel, add the three agent bots and yourself.
4. Post a bug report tagging triage-agent, then follow the same staged flow shown in the demo video.
