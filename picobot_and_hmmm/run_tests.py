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
    print "***** PicoBot: Empty Room Coverage *****"
    command = """python picobot.py -e env1.txt < empty_room.pb"""
    sought = """cells left: 0
Coverage reached!"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n...\n%s" %(sought)
    print "%s" %(ok() if got.endswith(sought) else "Got:\n%s\n%s" %(got, notok()))

def Problem2():
    print "***** Squared Distance *****"
    command = "echo 3 2 -1 5 | python hmmmSimulator.py -f squared_distance.b -n"
    sought = """25"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))

def Problem3():
    print "***** Sum of Ints *****"
    command = "echo 100 | python hmmmSimulator.py -f sum_of_ints.b -n"
    sought = """5050"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))

def Problem4():
    print "***** Primality Testing *****"
    command = "echo 31 | python hmmmSimulator.py -f primality.b -n"
    sought = """1"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))
    command = "echo 35 | python hmmmSimulator.py -f primality.b -n"
    sought = """0"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))

def Problem5():
    print "***** Euclid's Algorithm, Iterative Approach *****"
    command = "echo 54 24 | python hmmmSimulator.py -f gcd_iter.b -n"
    sought = """6"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))
    command = "echo 22 45 | python hmmmSimulator.py -f gcd_iter.b -n"
    sought = """1"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))

def Problem6():
    print "***** Euclid's Algorithm, Recursive Approach *****"
    command = "echo 54 24 | python hmmmSimulator.py -f gcd_rec.b -n"
    sought = """6"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))
    command = "echo 22 45 | python hmmmSimulator.py -f gcd_rec.b -n"
    sought = """1"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))

if __name__ == "__main__":
    colorama.init(autoreset = True)
    problems = [None, Problem1, Problem2, Problem3, Problem4, Problem5, 
                Problem6]
    args = map(int, sys.argv[1:])
    args = args if len(args) > 0 else range(1, len(problems))
    for i in args:
        problems[i]()
        print ""
