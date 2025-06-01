from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.document_template_list import DocumentTemplateList
from ...models.document_templateindex_order import DocumentTemplateindexOrder
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created_since: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    order: Unset | DocumentTemplateindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["created_since"] = created_since

    params["fields"] = fields

    params["ids[]"] = ids

    params["limit"] = limit

    json_order: Unset | str = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["page_token"] = page_token

    params["updated_since"] = updated_since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/document_templates.json",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DocumentTemplateList | Error | None:
    if response.status_code == 200:
        response_200 = DocumentTemplateList.from_dict(response.json())

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
    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DocumentTemplateList | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    created_since: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    order: Unset | DocumentTemplateindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[DocumentTemplateList | Error]:
    """Return the data for all DocumentTemplates

     Outlines the parameters, optional and required, used when requesting the data for all
    DocumentTemplates

    Args:
        created_since (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, DocumentTemplateindexOrder]):
        page_token (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DocumentTemplateList, Error]]
    """

    kwargs = _get_kwargs(
        created_since=created_since,
        fields=fields,
        ids=ids,
        limit=limit,
        order=order,
        page_token=page_token,
        updated_since=updated_since,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    created_since: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    order: Unset | DocumentTemplateindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> DocumentTemplateList | Error | None:
    """Return the data for all DocumentTemplates

     Outlines the parameters, optional and required, used when requesting the data for all
    DocumentTemplates

    Args:
        created_since (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, DocumentTemplateindexOrder]):
        page_token (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DocumentTemplateList, Error]
    """

    return sync_detailed(
        client=client,
        created_since=created_since,
        fields=fields,
        ids=ids,
        limit=limit,
        order=order,
        page_token=page_token,
        updated_since=updated_since,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    created_since: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    order: Unset | DocumentTemplateindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[DocumentTemplateList | Error]:
    """Return the data for all DocumentTemplates

     Outlines the parameters, optional and required, used when requesting the data for all
    DocumentTemplates

    Args:
        created_since (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, DocumentTemplateindexOrder]):
        page_token (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DocumentTemplateList, Error]]
    """

    kwargs = _get_kwargs(
        created_since=created_since,
        fields=fields,
        ids=ids,
        limit=limit,
        order=order,
        page_token=page_token,
        updated_since=updated_since,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    created_since: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    order: Unset | DocumentTemplateindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> DocumentTemplateList | Error | None:
    """Return the data for all DocumentTemplates

     Outlines the parameters, optional and required, used when requesting the data for all
    DocumentTemplates

    Args:
        created_since (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, DocumentTemplateindexOrder]):
        page_token (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DocumentTemplateList, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            created_since=created_since,
            fields=fields,
            ids=ids,
            limit=limit,
            order=order,
            page_token=page_token,
            updated_since=updated_since,
            x_api_version=x_api_version,
        )
    ).parsed
