{% extends "base_template.html" %}
{% block slideshow %}
name:agenda

# Introduction

This is a presentation about making slides with remark.

This is also session 1, called {{ name }}.

---

# Agenda

1. This is an ordered list
2. Sweet, right?

---

# Code example

The most important thing we'll be presenting is code. This tool makes that super easy.

```python
def hello_world():
    return "hello world"

if __name__ == '__main__':
    print(hello_world())
```

{% endblock %}
