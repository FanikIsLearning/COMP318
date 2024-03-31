data = [
    {
        "choices": [
            {"finish_reason": "stop", "index": 0, "logprobs": None, "text": " the sky?"}
        ],
        "created": 1637602374,
        "id": "cmpl-477TSTQ05oUrVJWBFHpPZmlaIpYHi",
        "model": "davinci:2020-05-03",
        "object": "text_completion",
    },
    {
        "choices": [
            {"finish_reason": "stop", "index": 0, "logprobs": None, "text": "Blue"}
        ],
        "created": 1637602375,
        "id": "cmpl-477TTCpAS31Sn2AgimqJyTMkvUAb8",
        "model": "davinci:2020-05-03",
        "object": "text_completion",
    },
    {
        "choices": [
            {
                "finish_reason": "stop",
                "index": 0,
                "logprobs": None,
                "text": "\nJupiter is a big planet. It's bigger than all the other planets. It's like a giant ball of gas.\n",
            }
        ],
        "created": 1637602375,
        "id": "cmpl-477TTY9Js3gFuoKLPiVXpW0L43Vig",
        "model": "davinci:2020-05-03",
        "object": "text_completion",
    },
]

for entry in data:
    for choice in entry["choices"]:
        print(choice["text"])
