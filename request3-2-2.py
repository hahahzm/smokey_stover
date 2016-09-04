import copy
import re
import sys
import time
#important
import collections

sys.setrecursionlimit(1024)

def make_trie(words):
    trie = collections.OrderedDict()
    for word in words:
        temp_trie = trie
        for letter in word:
            temp_trie = temp_trie.setdefault(letter, collections.OrderedDict())
        #temp_trie = temp_trie.setdefault('_end_', '_end_')
 
    return trie

def extract(trie, result):
    if trie:
        if len(trie) > 0:
            sub_result = []
            for char in trie.keys():
                sub_result.append(char)
            if sub_result not in result:
                result.append(sub_result)

        for char in trie.keys():
            #time.sleep(1)
            extract(trie[char], result)

def characters(queries):
    chars = []
    for query in queries:
        for char in query:
            if char not in chars:
                chars.append(char)
    return chars

def check(aplhabet, test):
    order = []
    for char in test:
        order.append(aplhabet.index(char))
    for i in range(len(order) - 1):
        if order[i] > order[i + 1]:
            return False
    return True

def cleanQuery(queries):
    q = []
    for query in queries:
        if (len(query) > 1):
            q.append(query)
    return q

def answer(words):
    # your code here
    trie = make_trie(words)

    queries = []

    extract(trie, queries)

    maximum = 0
    for query in queries:
        m = len(query)
        if m > maximum:
            maximum = m

    if maximum == 1:
        return str(queries[0][0])
    
    queries = cleanQuery(queries)

    for query in queries:
        print query

    all_char = characters(queries)

    q = copy.deepcopy(queries)

    lexical = []

    count = 0
    while queries:
        head = all_char[count % len(all_char)]
        if head not in lexical:
            switch = True
            for query in queries:
                if head in query and head != query[0]:
                    switch = False
                    break
            if switch:
                for query in queries:
                    while head in query:
                        query.remove(head)
                lexical.append(head)
        while [] in queries:
            queries.remove([])
        count += 1

    alp = []
    for char in lexical:
        alp.append(char)
    for qs in q:
        if not check(alp, qs):
            print "WRONG: ", qs

    result = ""
    for char in lexical:
        result += char
    return result

doc = """But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?
At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat
On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains
Central to Ford's ability to produce an affordable car was the development of the assembly line that increased the efficiency of manufacture and decreased its cost. Ford did not conceive the concept, he perfected it. Prior to the introduction of the assembly line, cars were individually crafted by teams of skilled workmen - a slow and expensive procedure. The assembly line reversed the process of automobile manufacture. Instead of workers going to the car, the car came to the worker who performed the same task of assembly over and over again. With the introduction and perfection of the process, Ford was able to reduce the assembly time of a Model T from twelve and a half hours to less than six hours.
Xylophones were probably one of peoples' first musical instruments, and the feel of playing them is most firmly entrenched in our primal core. I've seen babies barely able to pick up mallets know just what to do with them. 
Just about any one can make a xylophone out of just about anything- i.e. old shoes, cut up tires, bones, V.W. hoods, etc.... (official definition has a xylophone made of wood, so I guess we'd have to call them shodaphone, blimpaphone, bonaphone, volkphone, and et ceteraphone.) The main trick is just mounting whatever it is in a way that it will vibrate minimally hampered.

For the sake of simplicity, I'll describe the how-tos of building a wood xylophone, but the same techniques could be applied to any material. These instructions are intentionaly very general to promote creativity. For more detailed info there's some great books on basic instrument making.

Xylophone Tuning
Airbus have two vauseriants of the Zephyr designed to accommodate a variety of payload capacities.

Zephyr S is the name of the production variant of the Zephyr 8 vehicle.

The larger size of the Zephyr T (Twin) vehicle enables it to accommodate payloads with masses up to 20kg and continuous power in excess of 300W. A key feature of the Zephyr family is that they share common avionics, software, power flosystems, propulsion design and command and control and aero-structural design and elements. This means that production of the larger vehicle follows closely on the success of the Zephyr S.


First you take a chunk of wood (straight, clear, dense grain is ideal, but I've gotten neat sounds out of pretty gnarly looking stuff) and cut it to a length that suits. Too long or too short won't resonate very well, so experiment. Now, find the nodes by either measuring 22.5% of the length in from the ends or sprinkling some salt along the top and tapping it lightly- the salt will collect at the nodes. Support the wood under the nodes with something soft, like felt, foam, or balled up socks. Tune it by cutting it shorter to heighten the tone, or gouging under the middle to lower the tone. You can also raise the pitch slightly by thinning the ends, and lower the pitch by making a simple saw slice or gouge in the middle. The ideal shape for a xylophone bar is something like this: """

doc = "z yx yz"
words = doc.split(" ")

#words = sorted(re.findall("[a-z]+", doc.lower()))


print answer(words)
