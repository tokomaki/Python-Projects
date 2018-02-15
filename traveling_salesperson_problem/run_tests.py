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
    print "***** Tour Data Type *****"
    command = "python tour.py"
    sought = """Tour 1:~
(200.0, 400.0)
(300.0, 100.0)
(300.0, 200.0)
(100.0, 100.0)
Tour distance = 956.062330
Number of points = 4
Tour 2:~
(200.0, 400.0)
(100.0, 100.0)
(300.0, 100.0)
(300.0, 200.0)
Tour distance = 839.834564
Number of points = 4"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))

def Problem2():
    print "***** Nearest Neighbor Heuristic *****"
    command = "python nearest_insertion.py 5000 < data/tsp10.txt"
    sought = """(110.0, 225.0)
(161.0, 280.0)
(157.0, 443.0)
(283.0, 379.0)
(306.0, 360.0)
(325.0, 554.0)
(397.0, 566.0)
(490.0, 285.0)
(552.0, 199.0)
(343.0, 110.0)
Tour distance = 1566.136305
Number of points = 10"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))

def Problem3():
    print "***** Smallest Increase Heuristic *****"
    command = "python smallest_insertion.py 5000 < data/tsp10.txt"
    sought = """(110.0, 225.0)
(283.0, 379.0)
(306.0, 360.0)
(343.0, 110.0)
(552.0, 199.0)
(490.0, 285.0)
(397.0, 566.0)
(325.0, 554.0)
(157.0, 443.0)
(161.0, 280.0)
Tour distance = 1655.746186
Number of points = 10"""
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
