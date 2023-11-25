import argparse
import requests


def invoke_endpoint(url):
    headers = {
        "accept": "text/plain",
    }

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Request failed with status code:", response.status_code)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("username", type=str, help="Username")
    parser.add_argument("pipeline", type=str, help="Pipeline")

    args = parser.parse_args()

    url = f"http://crowdserv.sys.kth.se:8082/api/repo/exportyaml/{args.username}/{args.pipeline}"

    response = invoke_endpoint(url)

    print(response["data"])

    with open("pipeline.txt", "w") as f_out:
        f_out.write(response["data"])
