# Backend & Front = Antd + Parcel + Fastapi

## Include

- Front
  - React
  - TypeScript
  - Antd
  - Parcel
  - Less
  - Babel7
- Backend
  - Python
  - Fastapi

## Code
- add backend (*.py) into `backend` (like other fastapi app)
- add pages (*.html) into `public`
- add front into `src`

## Build

1. build front, see [README](README.md)
1. link the version
   - `ln -s debug dist` or `ln -s release dist`
1. start backend with front (as template & static)
   - `python asgi.py`


---

- [Parcel](https://parceljs.org/)
- [Antd](http://ant.design/)
- [Fastapi](https://fastapi.tiangolo.com/)
