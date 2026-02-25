# Transcript

[0:00] Okay, so a few hours ago, Anthropic 
released a brand new feature,
[0:03] which many people are calling Anthropic's own 
version of OpenClaw, OpenClaw for grownups,
[0:08] and now saying they don't even need to use 
OpenClaw or ClaudeBot anymore because they
[0:11] can just replicate the same thing inside of 
Claude Code. And this new feature is being able
[0:15] to control Claude Code running locally on your 
machine from your phone or another device. Now,
[0:20] you could have kind of done this before by using 
tmux, Tailscale, and also Terminus on your phone..
[0:25] And I've covered that before in 
my Claude Code Masterclass. But
[0:28] that was like kind of a hassle to do. 
And this update makes it much simpler
[0:31] because now you can just use a Claude 
Code app, kind like a messaging app.
[0:34] Now let's go for an example of how you can use 
this. Now you want to go to a folder. I'm going
[0:38] to go to my RayOS folder, which contains all 
my life stuff that I manage with Claude Code.
[0:44] And then do claude rc or claude 
remote-control. Press enter. And
[0:49] then that will spin up an instance of Claude Code.
[0:51] So the very first time you run it, you 
may see something like this where you
[0:54] have to enable it. And that opens a secure 
connection from your computer to Anthropic
[0:59] servers. Now I'm actually gonna run this 
in dangerously skip permissions instead.
[1:03] So let me stop that, do Claude dangerously 
skip permissions so it can do more things on
[1:08] my computer. And what I can do is do /remote 
control to enable it for this session. And
[1:12] if I want to enable it for every single 
session that I run in the future as well,
[1:16] I can do /config search for remote control.
[1:20] And it says enable remote control for 
all sessions. I'm going to change this
[1:24] to yes or true and then press 
Escape. And now remote control
[1:28] will be available for every session of 
Claude Code that I run in the future.
[1:31] So anyways, let's make sure that we have 
the Claude app installed, open it up,
[1:35] log into our account, then go to the code tab 
on the left-hand side and then find our session.
[1:41] Can you go to my Google Drive folder and then 
figure out where the raw MP4 file is and then
[1:46] edit the video with the, uh, video editor 
skill. So as soon as I send that message,
[1:51] you can see it now appears on my computer.
[1:52] So it's first going to go to my Google 
Drive, but I should have been a bit
[1:55] more specific because I have Google Drive 
set up locally. And recently I actually
[1:59] made a brand new skill for Claude Code to 
edit my videos for me. So this video that
[2:03] you're watching right now has been edited by 
Claude Code, but it's only like 95% perfect.
[2:07] So I still have to like clean 
up some loose ends myself. Um,
[2:10] but yeah, now you can see it's now 
downloading the video that I want
[2:13] edited. And whilst that's happening, 
I'm going to start a brand new session.
[2:16] So I could also be coding 
on projects, for example,
[2:18] like I have this project right over here 
and then I can remote control this session.
[2:22] Since I already had it enabled before, 
it's already enabled. So I can go back.
[2:26] Can you make the macOS release bump up the 
minor version? And yeah, that command sends
[2:30] off to my computer and it will work normally. 
Now the nice thing is that every time there is
[2:34] a permission that your computer requires because 
you're not in dangerously skip permissions,
[2:38] for example, you can allow it. And that 
is one of the benefits over using tmux
[2:42] and Terminus for this because it was like 
quite fiddly to allow it from your phone.
[2:46] Now, one of the benefits about this is that you 
have access to all your Claude Code config from
[2:51] your phone. So whatever skills you have set up, 
MCP servers and so forth. So if I run claude rc,
[2:57] then I can trigger plan mode and also the Exa 
MCP server that I have enabled from my phone.
[3:02] So let me go to the session over here. Switch 
over to plan mode. And if I press enter,
[3:07] you can see it's now using the Exa MCP 
server that I have set up on my computer.
[3:11] Now this means that you can have MCP server set 
up for background research tasks, for example,
[3:16] and then you can just be triggering the use of 
them from your phone. And now we can see that
[3:19] planning mode is asking us some questions 
that we can enter in from our phone. So I
[3:24] can just say like, hello, press submit, and 
I can answer a lot of questions that way.
[3:28] So that can be pretty helpful for just 
making plans on the go because you can go
[3:32] out for lunch and then continue working on 
your application. And now going back here,
[3:35] we can see Claude Code is still editing 
that video for us. So let's talk about
[3:38] the most important thing here, which is security.
[3:41] You don't want to be on bypass permissions 
or dangerously skip permissions all the
[3:45] time because that can get quite dangerous, 
especially if it's connected to internet.
[3:49] Now your version of Claude Code, which has 
remote control enabled, is connected securely
[3:54] via Anthropic's own servers to your phone 
or to another machine. So if I wanted to,
[3:58] I could go to the Claude AI website from 
another machine And then I can see that
[4:02] I have this remote session right now, which is 
the same session that is happening on my phone.
[4:06] And the server remote session is the one that 
is editing the video for us. But if I was kind
[4:10] of worried about it accidentally being prompt 
injected by searching online or deleting a file,
[4:14] I could either do one of two things, 
either use the Claude Code sandbox
[4:18] or have Claude Code running on a remote 
server somewhere. So I'll show you how
[4:22] you can install Claude Code on a remote 
server so you can have it run dangerously
[4:26] skip permissions over there and do like 
web research for you and stuff like that.
[4:29] Without worrying about it accidentally 
deleting your files or doing unintended
[4:33] things on your computer. So I'm 
gonna log into my Hetzner account
[4:36] and then just quickly set up a server for 
myself here. So you can do create server,
[4:40] choose the cheapest one, which is $3.49 a month. 
Choose— choose Germany over here, create my SSH
[4:48] key and add to that here. And then call the 
server Claude Code and press create and buy.
[4:52] And now what I can do is SSH into that server 
copy over the install command for Claude code,
[4:57] go back to the server, press enter. And 
then after it's installed, I can do Claude,
[5:01] press enter. But I actually have to 
copy over this command to fix the bash,
[5:08] do Claude, sign in with my Anthropic subscription.
[5:10] And then finally I can run tmux on the 
server, run Claude inside of tmux. Yes,
[5:15] I accept. Do /remote-control, enable 
remote control for the session..
[5:20] And then I can detach from this terminal 
session safely and have it running on the
[5:24] cloud. So if I press Ctrl+B and then 
type in colon detach, press Enter,
[5:30] then I can go back to my phone's version of Claude 
Code. And then I can see I have this interactive
[5:34] session and then I can chat with it and say stuff 
like searching online, tell me about Claude Code.
[5:39] So I could install my MCP servers onto this 
server and then have it continuously work
[5:44] for me in the background on different tasks 
and not have to worry about my computer being
[5:48] on all the time. So I can do research with 
different MCP servers, make reports for me,
[5:52] and even if it did get prompt injected, 
any damage that it does would be limited
[5:57] to the server that it's currently on. Now, 
another way of doing this is you can use
[6:00] sandboxing in Claude Code and have your remote 
control sessions run through that sandbox.
[6:05] So I cover much more about sandboxing in my 
master Claude Code class that will be linked
[6:09] down below if you're interested. 
But to give you a brief overview,
[6:12] if you make a folder like this and inside 
of your settings.local JSON file, you type
[6:18] in something like this, sandbox enabled 
true, permissions default mode don't ask.
[6:23] I can give it a list of websites I 
can just go to and do research on.
[6:26] And then I can deny any tools such as 
editing or writing tools, for example,
[6:30] and bash tools. And if I start a remote 
session of Claude Code here by doing claude rc,
[6:34] I can go to a session which is in the sandbox 
research environment here and then say,
[6:39] go on archive and find me the latest AI papers 
and summarize 5 that look interesting to you.
[6:44] You can see it can go and archive and 
not ask me for permissions because that
[6:48] is allowed over here. And then 
after pulling in the papers,
[6:50] it gave me some interesting summaries of them. 
So if I told it to fetch masterclaudecode.com,
[6:56] then you can see that it won't work because that 
URL has been blocked. But one of the problems can
[7:00] be that it may still decide to go on the website 
via a curl command, which can be dangerous. But
[7:05] in this case, it does not have access to 
bash tools, so it won't be able to do that.
[7:08] Now, one of the ways to make this stricter and 
more secure is to use a proxy. So for example,
[7:14] I would want it to be able to do curl requests,
[7:16] but I want to deny the WebFetch tool and the 
WebSearch tool because those would bypass the
[7:21] proxy. And then I should set up a network 
port over here. So that is HTTP proxy port.
[7:27] And then you want to make a proxy that looks 
kind of like this so you can get Claude Code
[7:31] to write you one. And you want to make sure 
that api.anthropic.com is allowed because
[7:36] that allows for the remote connection. Because 
if you don't, you may run into some problems.
[7:40] Now if I enable the proxy by doing node 
proxy.js, then do claude rc dangerously
[7:47] skip permissions. And then I can test out the 
proxy to make sure that it works by trying to
[7:52] go to my personal domain. So that should fail 
because, like, it's not allowed by the proxy.
[7:57] So you can see on the computer, it says 
HTTP GET blocked. But if I tell it to,
[8:02] like, do masterclaudecode.com instead,
[8:04] then that should work just fine 
because that is allowed by the proxy.
[8:07] So you can see, passed successfully via the 
proxy, and then it loaded in the page. So
[8:11] this is another way that you can make sure 
that you are using remote control securely,
[8:15] with dangerously skip permissions. So you could 
have like research agents that are only allowed
[8:20] to go on a set of websites, for example. You 
can also block a lot of permissions to prevent
[8:24] anything bad happening on your computer. 
And it's like really easy to customize.
[8:28] Now, one of the big differences 
from OpenClaw is that it's more
[8:31] passive and less proactive. So you can 
get OpenClaw to like search online at a
[8:35] scheduled interval for you. And then send 
you messages. Here it's more like passive,
[8:39] so you give it and tell it to do 
something, it does it for a while.
[8:42] But given how popular it's gotten, I imagine that 
Claude Code or the Anthropic team will slowly be
[8:47] adding them over time because it seems they kind 
of have an interest in the space. One feature that
[8:51] I would really like to see is basically the 
ability to connect hooks to notifications on
[8:56] your phone. So currently you can have Claude 
Code send you notifications on your computer
[9:01] using like Apple Scripts or something, but if 
Anthropic allowed for those notifications to be
[9:05] sent to your phone if you're remote controlling, 
I think that would make it even more powerful.
[9:09] But yeah, I'm sure they will be adding a lot more 
to it over time to improve it. Now it may be the
[9:13] case that you no longer need to use OpenClaw 
because this satisfies a lot of use cases for
[9:16] you. And I know for me personally, because I 
usually manage everything in my RayOS folder,
[9:21] the fact that I can now use this remotely 
from my phone means that I can just have
[9:24] it running all the time and then just be giving 
prompts to my RayOS folder to like draft emails,
[9:29] download files, do some video editing, 
and a bunch of other things as well,
[9:32] whilst using my Claude Code 
subscription to save on money.
[9:35] Now Claude Code has finished editing that 
video, so I'm going to get it to edit this
[9:38] video and then finally upload it. Anyways, 
I'm sure Anthropic I think will be making
[9:41] much more improvements here over time because 
they seem to be shipping a new update like
[9:44] almost every single day. And if you do want 
to get my own thoughts about it and ways in
[9:48] which I'm using it, then you can sign up to my 
newsletter, which will be linked down below.
[9:51] You do get access to a bunch 
of bonus free videos as well
[9:54] that you won't find here on the YouTube channel.
