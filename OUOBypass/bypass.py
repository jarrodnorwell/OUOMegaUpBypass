# ouo.io and ouo.press bypass code from https://github.com/xcscxr/ouo-bypass

from recaptcha import client, RecaptchaV3

import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def bypass(url: str) -> tuple[str, str]:
    tempurl = url.replace("ouo.press", "ouo.io")
    p = urlparse(tempurl)
    id = tempurl.split("/")[-1]
    res = client.get(tempurl, impersonate="chrome110")
    next_url = f"{p.scheme}://{p.hostname}/go/{id}"

    for _ in range(2):
        if res.headers.get("Location"):
            break

        bs4 = BeautifulSoup(res.content, "lxml")
        inputs = bs4.form.find_all("input", {"name": re.compile(r"token$")})
        data = {input.get("name"): input.get("value") for input in inputs}
        data["x-token"] = RecaptchaV3()

        h = {"content-type": "application/x-www-form-urlencoded"}

        res = client.post(
            next_url,
            data=data,
            headers=h,
            allow_redirects=False,
            impersonate="chrome110",
        )
        next_url = f"{p.scheme}://{p.hostname}/xreallcygo/{id}"

    return (url, res.headers.get("Location"))
