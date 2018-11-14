# Monitor the optimum

## Preface

In this fun and experimental research, I'll tell you a story of how you can
monitor the optimum. There are way too many metrics which you can collect and
process and most likely you already doing so. But one of the "things" that
I teach to my students when I'm helping them to go through the "Zabbix classes"
are: "Never let your monitoring platform tell you the facts. Your monitoring
must tell you the story of what's going on". And unfortunately, many very fine
administrators do surround themselves with just the facts, without caring for
what kind of story those facts are part of. They are looking at the CPU
consumption, or Garbage collection and use little of what they have to understand
the actual story behind the facts.

Why it is important ? I do like to make that example for my students: Everyone
knows about Chernobyl Power Plant failure. Well, you can call a thermal explosion
"a failure". Without going much into a nature of the event, the one fact,
very important to the monitoring practitioners from which we must learn. Computers in
1986 were much, much less powerful than, compare to now. The procedure and
a practice of the monitoring were different then, compare to now. The Engineer,
who controls a nuclear reactor were expected to manually monitor and process
about 2000 near-realtime metrics. It is very difficult, indeed. So, next time,
when you are looking at your Inbox, filled with thousands of the messages from
your monitoring platform, you must question yourself if you are doing things right. In
21 century, where cellphone in your pocket is much more powerful than computer
which monitors nuclear reactor in 1986, you must do better than this.

So, let's roll and find out how you can monitor the optimum. What is the optimum ?
The search for the optimum is the process of mathematical computations, in pursue
for the answer on the single question: "Which element are the best from the
selection of available alternatives". In most cases, we have to produce the
set of alternatives by running some computations.

When we are monitoring the metrics, the optimum calculated from some metrics and
criteria, often-time will tell us a story behind raw data. "Under the hood",
I will create the system of Linear Equations and will use the Simplex Algorithm
to search for the optimum. But have no fear. This presentation is done by
the System Administrator and for the fellow System Administrators.
I will try to make it simple.

When I mention the word "monitor", I did not mentioned it in wane. I will use
Zabbix monitoring platform as an example. Calculating the optimum is not the
functionality, supported by Zabbix "out of box". None of the monitoring platforms
I know about do that. We have to create a script,  which will collect data for
our computations and push the results back to the  platform which will do all
the "monitoring part".

So, some level of proficiency in coding, and particularly coding in Python will be
a pre-requirement. Also, you have to understand, this is a research and experiment.
Most likely, I will not deliver to you the solution, that you can use immediately.
This will be the "food for the thoughts". If you will produce any production-grade
solution, based on the ideas outlined in that research, and you will be able to
share that solution... You will do good for yourself and for the community of
monitoring practitioners.

## So, what we are going to do ?

We will do analysis of the resource allocation for the IT infrastructure with
minimization of the infrastructure cost.

Here is what's it's looks like:

* We are having a "products" which require some resources.
* Each product is running within known time constraints.
* We are having resources which are available for us.
* Each "unit" of the resource const us predefined amount of money.

We do need to monitor amount of resources required for the "products" and if our
infrastructure is cost-optimised or not.

## Requirements

* Python. I will use Python3, but there are nothing in  my code which is
specific to the Python3. At least, I don't think so. Since, this is a research,
feel free to use whatever version of the Python in your product, in which you are
most comfortable.
* PuLP module for the Python. You can install it with the __pip__. Exactly the
same way that you've installed all other Python modules.
```bash
pip3 install pulp
```
This module will do all [Linear Programming](https://en.wikipedia.org/wiki/Linear_programming) and
I find that it is somewhat simpler than the similar functionality in scipy.
But you can use ether.
* pyZabbix module, if you are serious about "talking to Zabbix"
```bash
pip3 install pyzabbix
```

## The Task.

Here is the facts that we will be using to build our model

### We have three "products"
* Product "A" is running 30 minutes per day and requires following resources:
1. 10 units of CPU
2. 4000 units of Memory
3. At least 250 units of Disk
* Product "B" is running 350 minutes per day and requires following resources:
1. 1000 units of CPU
2. 400 units of Memory
3. 50 units of Disk
* Product "C" is running 700 minutes per day and requires following resources:
1. 5 units of CPU
2. 40 units of Memory
3. At least 2000 units of Disk

### Here is the cost allocation for the resources:

* 1 unit of CPU costs us 0.02$ per minute
* 1 unit of the Memory costs us 0.05$ per minute
* 1 unit of the Disk costs us 0.01$ per minute.


# The Author

My name is Vladimir Ulogov, and I am System Administrator, Developer and engineer
with 25+ years of "working with computers". I spent 20+ years with monitoring
and 10+ years with Zabbix. While I am not the "Mr. Perfect", generally, I do know
what I am doing. I'll be glad to receive your opinions, updates and other
suggestions. Here is my LinkedIn: [https://www.linkedin.com/in/vladimirulogov/](https://www.linkedin.com/in/vladimirulogov/)
