import requests

class TestGood:
    def test_good416(self):
        r = requests.get('https://ticket-wus-b.browser.cloud.com/callsession/c98bjhbyjk88/health')
        print(r.status_code)
        print(r.json())
        print(r.text)
        assert r.status_code == 200
good1 = TestGood()
good1.test_good416()