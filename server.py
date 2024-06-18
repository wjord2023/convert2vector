import grpc
from concurrent import futures
import clip
import torch
import io
from PIL import Image
import numpy as np
import convert_pb2
import convert_pb2_grpc


class ClipService(convert_pb2_grpc.ClipServiceServicer):
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model, self.preprocess = clip.load("ViT-B/32", self.device)

    def GetImageVector(self, request, context):
        image_data = request.image
        image = Image.open(io.BytesIO(image_data))
        image = self.preprocess(image).unsqueeze(0).to(self.device)
        with torch.no_grad():
            image_features = self.model.encode_image(image)
        return convert_pb2.VectorResponse(
            vector=image_features.cpu().numpy().flatten().tolist()
        )

    def GetTextVector(self, request, context):
        text = request.text
        with torch.no_grad():
            text_features = self.model.encode_text(
                clip.tokenize([text]).to(self.device)
            )
        return convert_pb2.VectorResponse(
            vector=text_features.cpu().numpy().flatten().tolist()
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    convert_pb2_grpc.add_ClipServiceServicer_to_server(ClipService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
