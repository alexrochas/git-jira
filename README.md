# git-jira
> minor python function to extract Jira ticket number and add to git commits

## What?

Imagine that you have a branch with name **[place_holder]-1234** and you always forget to put the ticket number in your commit message?

Now, no more!

## How?

Add a new alias to your zsh/bash/fish:

```bash
alias git-jira='[path_to_script]/git_commit.py'
```

Now just use it as you would with *git commit*.

```bash
~/[some_path]$ git-jira "commit message" 
```

And voilà!

## Meta

Alex Rocha - [about.me](http://about.me/alex.rochas) -
