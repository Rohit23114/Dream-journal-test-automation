from config import setup_driver, cleanup, WEBSITE_URL
import openai
import os
from dotenv import load_dotenv

def test_ai_classification():
    print("\nTesting AI Classification (Optional)...")
    load_dotenv()
    
    if not os.getenv("OPENAI_API_KEY"):
        print(" - No API key found, skipping AI tests")
        return False

    driver, wait = setup_driver()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    try:
        driver.get(WEBSITE_URL + "dreams-diary.html")
        dreams = driver.find_elements(By.CSS_SELECTOR, "table#dreamTable tbody tr")[:3]
        for dream in dreams:
            name = dream.find_elements(By.TAG_NAME, "td")[0].text
            actual_type = dream.find_elements(By.TAG_NAME, "td")[2].text
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{
                    "role": "system", 
                    "content": "Respond with just 'Good' or 'Bad' for this dream:"
                }, {
                    "role": "user", 
                    "content": name
                }]
            )
            
            ai_type = response.choices[0].message.content.strip()
            print(f" - Dream: '{name}'")
            print(f"   Page: {actual_type}, AI: {ai_type}")

        print("AI tests completed!")
        return True
        
    except Exception as e:
        print(f"AI test failed: {e}")
        return False
    finally:
        cleanup(driver)

if __name__ == "__main__":
    test_ai_classification()
