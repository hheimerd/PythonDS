from analytics import Research, Analytics
from config import CONFIG 

def on_error(message):
    print(message)
    exit()

def main():
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
    
    anal.save_file(report, CONFIG['output_file_name'], CONFIG['output_file_ext'])
    


if __name__ == "__main__":
    main()