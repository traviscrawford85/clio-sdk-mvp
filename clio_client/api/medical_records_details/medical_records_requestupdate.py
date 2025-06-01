from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.medical_records_request_show import MedicalRecordsRequestShow
from ...models.medical_records_requestupdate_data_body import (
    MedicalRecordsRequestupdateDataBody,
)
from ...models.medical_records_requestupdate_files_body import (
    MedicalRecordsRequestupdateFilesBody,
)
from ...models.medical_records_requestupdate_json_body import (
    MedicalRecordsRequestupdateJsonBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    body: MedicalRecordsRequestupdateJsonBody
    | MedicalRecordsRequestupdateDataBody
    | MedicalRecordsRequestupdateFilesBody,
    fields: Unset | str = UNSET,
    if_match: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["IF-MATCH"] = if_match

    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/medical_records_details/{id}.json",
        "params": params,
    }

    if isinstance(body, MedicalRecordsRequestupdateJsonBody):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, MedicalRecordsRequestupdateDataBody):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, MedicalRecordsRequestupdateFilesBody):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | MedicalRecordsRequestShow | None:
    if response.status_code == 200:
        response_200 = MedicalRecordsRequestShow.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == 412:
        response_412 = Error.from_dict(response.json())

        return response_412
    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422
    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | MedicalRecordsRequestShow]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: MedicalRecordsRequestupdateJsonBody
    | MedicalRecordsRequestupdateDataBody
    | MedicalRecordsRequestupdateFilesBody,
    fields: Unset | str = UNSET,
    if_match: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[Error | MedicalRecordsRequestShow]:
    """Updating a Medical Records Detail

     If there are records being passed into the Medical Records or Medical Bills parameter they will be
    treated
    as new records and new Medical Records / Medical Bills will be created.

    Args:
        id (int):
        fields (Union[Unset, str]):
        if_match (Union[Unset, str]):
        x_api_version (Union[Unset, str]):
        body (MedicalRecordsRequestupdateJsonBody):
        body (MedicalRecordsRequestupdateDataBody):
        body (MedicalRecordsRequestupdateFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MedicalRecordsRequestShow]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        fields=fields,
        if_match=if_match,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: MedicalRecordsRequestupdateJsonBody
    | MedicalRecordsRequestupdateDataBody
    | MedicalRecordsRequestupdateFilesBody,
    fields: Unset | str = UNSET,
    if_match: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Error | MedicalRecordsRequestShow | None:
    """Updating a Medical Records Detail

     If there are records being passed into the Medical Records or Medical Bills parameter they will be
    treated
    as new records and new Medical Records / Medical Bills will be created.

    Args:
        id (int):
        fields (Union[Unset, str]):
        if_match (Union[Unset, str]):
        x_api_version (Union[Unset, str]):
        body (MedicalRecordsRequestupdateJsonBody):
        body (MedicalRecordsRequestupdateDataBody):
        body (MedicalRecordsRequestupdateFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MedicalRecordsRequestShow]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        fields=fields,
        if_match=if_match,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: MedicalRecordsRequestupdateJsonBody
    | MedicalRecordsRequestupdateDataBody
    | MedicalRecordsRequestupdateFilesBody,
    fields: Unset | str = UNSET,
    if_match: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[Error | MedicalRecordsRequestShow]:
    """Updating a Medical Records Detail

     If there are records being passed into the Medical Records or Medical Bills parameter they will be
    treated
    as new records and new Medical Records / Medical Bills will be created.

    Args:
        id (int):
        fields (Union[Unset, str]):
        if_match (Union[Unset, str]):
        x_api_version (Union[Unset, str]):
        body (MedicalRecordsRequestupdateJsonBody):
        body (MedicalRecordsRequestupdateDataBody):
        body (MedicalRecordsRequestupdateFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, MedicalRecordsRequestShow]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        fields=fields,
        if_match=if_match,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: MedicalRecordsRequestupdateJsonBody
    | MedicalRecordsRequestupdateDataBody
    | MedicalRecordsRequestupdateFilesBody,
    fields: Unset | str = UNSET,
    if_match: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Error | MedicalRecordsRequestShow | None:
    """Updating a Medical Records Detail

     If there are records being passed into the Medical Records or Medical Bills parameter they will be
    treated
    as new records and new Medical Records / Medical Bills will be created.

    Args:
        id (int):
        fields (Union[Unset, str]):
        if_match (Union[Unset, str]):
        x_api_version (Union[Unset, str]):
        body (MedicalRecordsRequestupdateJsonBody):
        body (MedicalRecordsRequestupdateDataBody):
        body (MedicalRecordsRequestupdateFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, MedicalRecordsRequestShow]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            fields=fields,
            if_match=if_match,
            x_api_version=x_api_version,
        )
    ).parsed
