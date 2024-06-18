import grpc
import convert_pb2
import convert_pb2_grpc
import io
from PIL import Image

def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = convert_pb2_grpc.ClipServiceStub(channel)

    # 测试图片向量
    with open("cat0.jpeg", "rb") as f:
        image_data = f.read()
    image_request = convert_pb2.ImageRequest(image=image_data)
    image_response = stub.GetImageVector(image_request)
    image_response_vector = image_response.vector
    print("Image Vector:", len(image_response.vector))

    # 测试文字向量
    text_request = convert_pb2.TextRequest(text="A sample text")
    text_response = stub.GetTextVector(text_request)
    print("Text Vector:", text_response.vector)


if __name__ == "__main__":
    run()
