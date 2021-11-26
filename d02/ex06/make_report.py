from analytics import Research, Analytics
from config import CONFIG 
import logging
import json
import requests

def on_error(message):
    print(message)
    exit()

def main():
    if CONFIG["log_file"]:
        logging.basicConfig(level=logging.DEBUG, 
                            format='%(asctime)s,%(msecs)03d %(message)s',
                            datefmt='%Y-%m-%d %I:%M:%S',
                            filename=CONFIG["log_file"])
    
    researcher = Research(CONFIG['input_file'])

    try:
        lines = researcher.file_reader()
    except IOError:
        on_error('File not found')
    except Exception:
        on_error("ValueError")
    
    
    anal = Analytics(lines)
    count = anal.counts(lines)
    fractions = anal.fractions(count)
    
    rand_tossing = anal.predict_random(CONFIG["num_of_steps"])
    rand_count = anal.counts(rand_tossing)
    
    report = CONFIG["report_message"].format(len(lines), 
                                          count[1], count[0], 
                                          round(fractions[1], 2), round(fractions[0], 2), 
                                          CONFIG["num_of_steps"], 
                                          rand_count[1], rand_count[0])
    
    dto = {
        "token": CONFIG['slack_token'],
        "channel": CONFIG['channel_id'],
        "text": report
    }
    
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": f"Bearer {CONFIG['slack_token']}"
    }
    
    serp = requests.post('https://slack.com/api/chat.postMessage', json.dumps(dto), headers=headers)
    
    print(serp.json())
    


if __name__ == "__main__":
    main()