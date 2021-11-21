# toxic_detection_bot_endpoint

This repository is used in the Junction 2021 event, in parallel with this [repo](https://github.com/longv/chat-police-bot), to facilitate a Discord bot to help nurture good behaviour in game chat, or just online chat in general.

The model and actual functionality was done on the other repository. This repository took the output model and serve it through a RESTful endpoint to bypass the compatibility issue we faced while working on the hackathon.

This endpoint is simple and only take in 1 type of request: `/predict`

And the only required param is `sentence` which expecting a string of text, a message of sort.

The endpoint will then refer to the Keras model trained previously to output a json of category-probability pairs, i.e.:

```
{
    "toxic": 0.95,
    "severe_toxic": 0.78,
    "obscene": 0.004,
    "threat": 0.5,
    "insult": 0.98,
    "identity_hate": 0.1,
}
```

### To deploy locally, run:
`pip install -r requirement.txt`

At the point of this writing, Tensorflow 2.4.1 is not compatible with MacOS M1, replace your tensorflow package with one tailor made for M1, i.e. refer to this [thread](https://stackoverflow.com/a/68214296) on stackoverflow.

Then run in the directory of `app.py`:

`python app.py`

### This can also be used to deploy to Google Cloud Run
Build: `gcloud build submit --tag eu.gcr.io/$YOUR_PROJECT_ID/$YOUR_IMAGE_NAME:$AND_TAG`

Deploy to Cloud Run:

```
gcloud run deploy $YOUR_SERVICE_NAME \
    --image eu.gcr.io/$YOUR_PROJECT_ID/$YOUR_IMAGE_NAME:$AND_TAG \
    --region europe-west1 \
    --allow-unauthenticated # If this is a public endpoint, like this one
```
