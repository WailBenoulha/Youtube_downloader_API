import os
from pytube import YouTube
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DownloaderSerializer

class DownloaderView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DownloaderSerializer(data=request.data)
        if serializer.is_valid():
            link = serializer.validated_data['link']
            try:
                # Log the received link
                print(f"Received link: {link}")

                video = YouTube(link)
                stream = video.streams.get_lowest_resolution()

                # Log the selected stream
                print(f"Selected stream: {stream}")

                # Define a download directory
                download_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
                if not os.path.exists(download_dir):
                    os.makedirs(download_dir)

                # Log the download path
                print(f"Downloading to: {download_dir}")

                # Download the video
                stream.download(output_path=download_dir)

                # Log success message
                print("Download successful")

                return Response({'message': 'Download successful'}, status=status.HTTP_200_OK)
            except Exception as e:
                # Log the exception
                print(f"Download failed: {str(e)}")
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Log invalid serializer data
            print(f"Invalid data: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
