# Observer Pattern

The Observer pattern defines a one-to-many relationship between objects.

When a subject produces an event, all registered observers are notified.

## Core idea

```text
Subject
  emits an event
      ↓
Observers
  react to the event
