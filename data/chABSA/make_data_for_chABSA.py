import random
import csv
import pprint

def load_data(filepath, targets):
    comments = []
    tmp_comments = []
    with open(filepath, "rb") as f:
        for l in f:
            l_utf8 = l.decode('utf-8')
            print(l_utf8)
            comment = [str(ord(x)) for x in l_utf8]
            print(comment)
            title = comment[0]
            #tmp_comments.append('{0},"{1}","{2}"'.format(targets, title, " ".join(comment)))
            tmp_comments.append([int(targets), str(title), " ".join(comment)])
            print('{0},"{1}","{2}"'.format(targets, title, " ".join(comment)))
    return tmp_comments
    
def write_csv(filename, tmp_comments):
    with open(filename, 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for row_text in tmp_comments:
            writer.writerow(row_text)


filepath_pos = "chABSA/pos.txt"
filepath_neg = "chABSA/neg.txt"

output_comments = []

output_comments += load_data(filepath_pos,1)
output_comments += load_data(filepath_neg,2)
random.shuffle(output_comments)

print(len(output_comments))
rate_number = int(len(output_comments) * 0.8)
print(rate_number)

train_comments = output_comments[:rate_number]
test_comments = output_comments[rate_number:]

write_csv("chABSA/train.csv", train_comments)
write_csv("chABSA/test.csv", test_comments)
