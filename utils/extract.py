import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_fashion_studio(pages=50):
   
    base_url = "https://fashion-studio.dicoding.dev/page{}"
    results = []
    for page in range(1, pages + 1):
        try:
            url = base_url.format(page) if page > 1 else "https://fashion-studio.dicoding.dev/"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            products = soup.find_all("div", class_="collection-card")
            timestamp = datetime.now().isoformat()
            for product in products:
                try:
                    title = product.find("h3", class_="product-title").get_text(strip=True)
                    
                    price_tag = product.find("span", class_="price")
                    if not price_tag:
                        price_tag = product.find("p", class_="price")
                    price = price_tag.get_text(strip=True) if price_tag else None

                    # Ambil semua <p> di product-details
                    p_tags = product.find_all("p")
                    rating, colors, size, gender = None, None, None, None
                    for p in p_tags:
                        text = p.get_text(strip=True)
                        if "Rating:" in text:
                            rating = text.replace("Rating:", "").replace("⭐", "").replace("/ 5", "").strip()
                        elif "Colors" in text:
                            colors = text.replace("Colors", "").replace("Colors", "").strip()
                            # Atau ambil angka saja
                            colors = ''.join(filter(str.isdigit, text))
                        elif "Size:" in text:
                            size = text.replace("Size:", "").strip()
                        elif "Gender:" in text:
                            gender = text.replace("Gender:", "").strip()
                    results.append({
                        "Title": title,
                        "Price": price,
                        "Rating": rating,
                        "Colors": colors,
                        "Size": size,
                        "Gender": gender,
                        "timestamp": timestamp
                    })
                except Exception as e:
                    continue
            print(f"Scraping halaman {page} berhasil. Jumlah produk: {len(products)}")
            
            # Error Handling
        except Exception as e:
            print(f"Error scraping page {page}: {e}")
            continue
    print(f"Scraping selesai. Total data produk: {len(results)}")
    return results