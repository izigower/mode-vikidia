<div align="center">

<a href="README.md">🇫🇷 Français</a> · <b>🇬🇧 English</b>

# mode-vikidia

**Your AI explains everything like a Vikidia article:<br>short sentences, hard words explained, real-life examples.**

<img src="demo/demo-en.gif" alt="Before / after: the same question asked without and with /vikidia" width="880">

<sub>Same question, same AI. Readability measured with <a href="evals/lisibilite.py">Flesch Reading Ease</a>: 10 → 67 out of 100.</sub>

</div>

---

## Why?

AI assistants answer like Wikipedia: accurate, but often unreadable when
you're new to a topic. [Vikidia](https://en.vikidia.org), the encyclopedia
for 8 to 13 year olds, shows you can explain anything clearly **without
talking down to people**. This skill teaches your AI that style.

The project started in French, where nothing like it existed. The skill
**answers in the language of your question**, so it works just as well in
English.

## Install

### Claude Code (2 commands)

```
/plugin marketplace add izigower/mode-vikidia
/plugin install mode-vikidia@mode-vikidia
```

Or by hand: copy `skills/vikidia/` into `~/.claude/skills/`.

### Claude.ai

Settings → Capabilities → Skills → upload the `skills/vikidia` folder as a zip.

### ChatGPT, Gemini, Mistral…

Paste [prompts/universal-en.md](prompts/universal-en.md) into your custom
instructions, or at the start of a conversation.

## Usage

| You type | You get |
|---|---|
| `/vikidia what is an API?` | an answer in Vikidia style |
| `vikidia mode` | the rest of the conversation in Vikidia style |
| `normal mode` | back to regular answers |
| `/vikidia 8ans photosynthesis` | even simpler (age 8) |
| `/vikidia ado blockchain` | a bit more technical (teens) |
| "I don't get it" | the skill kicks in on its own |

## The 8 rules

1. The first sentence **defines**.
2. **One idea** per sentence.
3. Every hard word is **explained** on the spot.
4. Go from the **known** to the unknown.
5. One **everyday example**.
6. An **encyclopedia** tone, never childish.
7. **True**, even when simplified.
8. **Short**: it fits on one screen.

## Vikidia as a source

When the AI needs to look something up, it reads **Vikidia** first, in the
language of your question, through its API. If the article doesn't exist in
that language, it reads the French version (the largest edition) and rewrites
it in English. Simple English Wikipedia and Wikipedia come last, and the
source is always cited.

## Gallery

[galerie/](galerie/) collects the best explanations made with the skill.
**Add yours**: open a PR with your question, the answer and its readability
score (`python3 evals/lisibilite.py --en answer.txt`). Details in
[CONTRIBUTING.md](CONTRIBUTING.md).

---

<sub>Independent project, inspired by Vikidia's style and not affiliated
with the Vikidia association. MIT License. Made with Claude Code.</sub>
