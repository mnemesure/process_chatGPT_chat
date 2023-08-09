import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_html_from_GPT_link(url):
    """
    Function to get all HTML from GPT share link
    """
    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        raise e
    

def get_all_messages(response):
    """
    Get only the divs with messages from the full HTML
    """
    partial_class_for_message_div = "group w-full text-token-text-primary"
    soup = BeautifulSoup(response, 'html.parser')
    divs = soup.find_all('div', 
                         attrs={
                             'class': lambda e: e.startswith(partial_class_for_message_div) if e else False
                            }
                        )
    return divs


def generate_message_data(all_divs):
    """
    Take all divs, loop through and process text plus sender.
    """
    final_data_structure_as_dict = {
        'message_number':[],
        'message_content':[],
        'generator':[]
    }

    for message_num, div in enumerate(all_divs):
        no_para = div.find_all('div', attrs={'class': "empty:hidden"})
        para = div.find_all('p')

        if no_para:
            final_data_structure_as_dict['message_content'].append(no_para[0].text)
        elif para:
            full_text = '\n'.join([element.text for element in para])
            final_data_structure_as_dict['message_content'].append(full_text)
        else:
            raise ValueError("Message content was not found")
        
        if div.find_all('title'):
            final_data_structure_as_dict['generator'].append('GPT')
        else:
            final_data_structure_as_dict['generator'].append('Human')
        
        final_data_structure_as_dict['message_number'].append(message_num)

    return final_data_structure_as_dict


def save_output(final_data_struct,url):
    data_for_csv = pd.DataFrame(final_data_struct)
    data_for_csv.to_csv(f"{url.split('/')[-1]}.csv",index=False)
    
    print(f"{url.split('/')[-1]}.csv saved successfully")

if __name__=="__main__":
    url = "https://chat.openai.com/share/e2b77f39-4b58-44e3-8523-9529c817af64"
    all_html = get_html_from_GPT_link(url)
    message_divs = get_all_messages(all_html)
    final_data = generate_message_data(message_divs)
    save_output(final_data, url)

