from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse

firmware = APIRouter(prefix='/firmware', tags=['firmware'])

firmware_version: str = ''

@firmware.post('/set-version')
async def set_version(version: str):
    global firmware_version

    preview_version = firmware_version
    firmware_version = version

    return {
        'message': 'version updated!',
        'preview version': preview_version,
        'atual version': firmware_version
    }

@firmware.get('/')
async def get_firmware_version():
    global firmware_version

    return {
        'version': firmware_version
    }

@firmware.get('/download')
async def download_firmware():
    return FileResponse(
        path="firmwares/firmware.bin",
        filename="firmware.bin",
        media_type="application/octet-stream"
    )

@firmware.post('/update')
async def update_firmware(firmware: UploadFile = File(...)):
    file_path = f'./firmwares/{firmware.filename}'
    
    with open(file_path, 'wb') as f:
        content = await firmware.read()
        f.write(content)
    
    return {
        "filename": firmware.filename,
        "content_type": firmware.content_type,
        "status": "upload concluído"
    }