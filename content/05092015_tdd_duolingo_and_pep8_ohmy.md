Title: TDD, using Duolingo, and PEP8 formatting
Date: 2015-05-09
Tags: human language, computer language, french, python, tdd, testing
slug: tdd_duolingo_and_pep8_ohmy
Summary: What I now know about each, from the past week or more
Category: Weekly Roundup

Wow, it's been almost a month since my last post. Getting into a groove of regular writing can be tough, so I thought it made sense to switch gears a little and reflect on what I happened to learn in a given week (or so).

###TDD
TDD, or [Test-Driven Development](http://en.wikipedia.org/wiki/Test-driven_development), has been on my radar ever since I heard of Harry Percivel's book on [TDD in Python](http://www.obeythetestinggoat.com/). A very cursory reading reveals that it's nothing more than the idea of

1. Write a test before writing code
2. Write code that will make the test pass
3. Refactor the code
4. Repeat

That didn't really mean a whole lot to me though. The idea of writing a test before code seemed counter-intuitive. And what are all these testing frameworks? I finally watched the [Lynda.com course on TDD](http://www.lynda.com/Developer-Programming-Foundations-tutorials/Foundations-Programming-Test-Driven-Development/124398-2.html) and it all started to click! In deciding on the tests, you're both organizing your code, and (hopefully) preventing the introduction of breaking changes. At least, you can identify those changes early, and locate them precisely.

This practice would have been a big help on my first project in my current job. The code base isn't very large - just one JavaScript file with a bunch of methods - but it still got confusing pretty quickly. And looking at the code, I can see where I have methods that are doing several different important things, making them very difficult to test. TDD could have also saved me the headache of redoing a bunch of manual tests every time I made a change.

Ladies Who Code DC had a Meetup on [Learning Programming through TDD](http://www.meetup.com/Ladies-Who-Code-Washington-DC/events/195560302/) this past week, which was very helpful in practicing my newly learned skill. We did pair programming, and I was able to work with someone who's been using TDD at work for a few months. It was a great learning experience, and I look forward to employing the method in my personal and work projects in the future. Who knows, maybe I'll even get a chance to refactor that first bit of JavaScript code from projects past.

###Duolingo
In my first post on learning French, I stated my intent to use the Fluent Forever method. Well, I did make it through the minimal pairs and pronunciation decks I purchased, but have stalled out on making all the flash cards for vocabulary. It's been taking much longer than I anticipated, and quite frankly, I find it really boring. Especially when I have other things I could be doing that feel either more productive or more interesting.

I tried thinking up ways to automate the task, but ultimately decided against it. The primary thing I want to do away with is having to choose the images for words/phrases one by one. However, doing so is genuinely useful for learning, and I would likely have to go back to choose new images when what I auto-collected wasn't on target. It might end up taking as much or more time than doing the selection by hand.

Enter [Duolingo](https://www.duolingo.com/). If you don't know about Duolingo, it's a free web and mobile language learning platform. They have been adding a bunch of new languages (Klingon is coming soon) and it's a really robust product. I used it briefly prior to going to Paris a few years ago, and really enjoyed it then. They've made improvements since that time, and I just think it's a great product. The main selling point(s) are being able to jump right in, no prep work required, and the cost.

I'm not going at a breakneck pace. Just spending some time every day first reviewing what I've learned previously, then doing a few new lessons. I'm still slowly gathering the materials for the flash cards a la Fluent Forever, but I wanted to be actively learning while doing so. And podcasts continue to be a good way to practice listening, since the robot voice in Duolingo can be a bit odd. Not to mention that you're only getting a single word or sentence at a time.


###PEP8
PEP8 is the [style guide for Python](https://www.python.org/dev/peps/pep-0008/). Super exciting I know. Well, the other day, an acquaintance was telling me about the many aggravating discussions that happen over coding style at his job. He suggested using PEP8, and built a little tool that everyone could use to clean up their code according to those standards. It appears disagreements continue for him, but I thought that was a pretty smart idea.

Since I use Sublime Text as my text editor at home. I installed the [AutoPEP8 package](https://github.com/wistful/SublimeAutoPEP8) and it's really easy to use. You can just change the code, or run a preview first. On Linus the shortcuts are `ctrl + shift + 8` to reformat my code, and `ctrl + 8` to show a preview of what's to be changed. The preview functionality looks a bit like changes shown with git. For instance, I tried putting two lines on one, separating them by a ;. Here's what the reformatting preview looks like:

```python
     def test_Add_method_multiple_string(self):
-        numList = [str(num) for num in range(0, 100, 5)];numString = ','.join(numList)
+        numList = [str(num) for num in range(0, 100, 5)]
+        numString = ','.join(numList)
         self.assertEqual(Calculator().add(numString), sum(range(0, 100, 5)))
```

That's easy enough! The line with a `-` will be removed, and the lines with the `+` will be added. Cool!

**Resources**:

- [TDD in Python Book](http://www.obeythetestinggoat.com/)
- [Lynda.com course on TDD](http://www.lynda.com/Developer-Programming-Foundations-tutorials/Foundations-Programming-Test-Driven-Development/124398-2.html)
- [Duolingo](https://www.duolingo.com/)
- [PEP8](https://www.python.org/dev/peps/pep-0008/)
- [AutoPEP8 package for Sublime Text](https://github.com/wistful/SublimeAutoPEP8)