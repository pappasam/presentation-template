{% extends "base_template.html" %}
{% block slideshow %}
name:agenda

# Introduction

This is a presentation about making slides with remark.

This is also session 1, called {{ name }}.

???

# Note 1

1. Hello
2. World

---

# Agenda

1. This is an ordered list
2. Sweet, right?

---

# Code example

The most important thing we'll be presenting is code. This tool makes that super easy.

```python
def hello():
    '''Return the string 'hello' '''
    return "hello"

def world():
    '''Return the string 'world' '''
    return "world"

def hello_world():
    '''Return the string 'hello world' '''
    return "{} {}".format(hello(), world())

if __name__ == '__main__':
    print(hello_world())
```

{% endblock %}
