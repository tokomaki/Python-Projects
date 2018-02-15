import colorama, datetime, os, shlex, signal, subprocess, sys, time

def run(command_chain, timeout = 30):
    """
    Runs the specified command chain and returns (True, <output>) on success. 
    If the command doesn't return within the specified time (in seconds), 
    (False, "") is returned. 
    """

    command_list = command_chain.split("|")
    start = datetime.datetime.now()
    process = None
    for command in command_list:
        tokens = shlex.split(command.strip())
        program = []
        for token in tokens:
            if token == "<" or token == ">":
                break
            program.append(token)
        stdin = None if not "<" in tokens \
                else open(tokens[tokens.index("<") + 1], "r")
        stdout = subprocess.PIPE if not ">" in tokens \
                 else open(tokens[tokens.index(">") + 1], "w")
        if process == None:
            process = subprocess.Popen(program, stdin = stdin, 
                                       stdout = stdout, 
                                       stderr = subprocess.STDOUT)
        else:
            process = subprocess.Popen(program, stdin = process.stdout, 
                                       stdout = stdout, 
                                       stderr = subprocess.STDOUT)
    while process.poll() is None:
        time.sleep(0.1)
        now = datetime.datetime.now()
        if (now - start).seconds > timeout:
            os.kill(process.pid, signal.SIGKILL)
            os.waitpid(-1, os.WNOHANG)
            return False, ""
    return (True, process.stdout.read().strip().replace("\r\n", "\n")) \
        if process.stdout != None else (True, "")
    
def ok():
    """
    Returns the string "Pass" in green.
    """
    return "%sPass" %(colorama.Fore.GREEN)

def notok():
    """
    Returns the string "Fail" in red.
    """

    return "%sFail" %(colorama.Fore.RED)

def Problem1():
    print "***** Markov Model Data Type *****"
    command = "python markov_model.py"
    sought = """text: banana, k = 2
freq('an', 'a')  = 2
freq('na', 'b')  = 1
freq('na', 'a')  = 0
freq('na')       = 2

text: one fish two fish red fish blue fish, k = 4
freq('ish ', 'r') = 1
freq('ish ', '0') = 0
freq('ish ')      = 3
freq('tuna')      = 0

text: gagggagaggcgagaaa, k = 2
freq('aa', 'a') = 1
freq('ga', 'g') = 4
freq('gg', 'c') = 1
freq('ag')      = 5
freq('cg')      = 1
freq('gc')      = 1"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))

def Problem2():
    print "***** Random Text Generator *****"
    print "Must be tested manually"

def Problem3():
    print "***** Noisy Message Decoder *****"
    command = "python fix_corrupted.py 4 \"it w~s th~ bes~ of tim~s, i~ was ~he wo~st of~times.\" < data/obama.txt"
    sought = """it was the best of times, it was the worst of times."""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))
    command = "python fix_corrupted.py 2 \"it w~s th~ bes~ of tim~s, i~ was ~he wo~st of~times.\" < data/obama.txt"
    sought = """it was the best of times, is was the worst of times."""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))

if __name__ == "__main__":
    colorama.init(autoreset = True)
    problems = [None, Problem1, Problem2, Problem3]
    args = map(int, sys.argv[1:])
    args = args if len(args) > 0 else range(1, len(problems))
    for i in args:
        problems[i]()
        print ""
