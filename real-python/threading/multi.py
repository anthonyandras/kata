import multiprocessing
import time
import requests

session = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def download_site(url):
    with session.get(url) as response:
        indicator = "J" if "jython" in url else "R"
        print(indicator, sep='', end='', flush=True)


def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)


if __name__ == '__main__':
    sites = [
                "https://www.jython.org",
                "http://olympus.realpython.org/dice"
            ] * 80

    print("Starting downloads")
    start = time.time()
    download_all_sites(sites)
    duration = time.time() - start
    print(f"\nDownloaded {len(sites)} sites in {duration} seconds")
