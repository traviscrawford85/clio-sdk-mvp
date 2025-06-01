from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.folder_list import FolderList
from ...models.folderindex_order import FolderindexOrder
from ...models.folderindex_scope import FolderindexScope
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    contact_id: Unset | int = UNSET,
    created_since: Unset | str = UNSET,
    document_category_id: Unset | int = UNSET,
    external_property_name: Unset | str = UNSET,
    external_property_value: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    include_deleted: Unset | bool = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    order: Unset | FolderindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    parent_id: Unset | int = UNSET,
    query: Unset | str = UNSET,
    scope: Unset | FolderindexScope = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["contact_id"] = contact_id

    params["created_since"] = created_since

    params["document_category_id"] = document_category_id

    params["external_property_name"] = external_property_name

    params["external_property_value"] = external_property_value

    params["fields"] = fields

    params["ids[]"] = ids

    params["include_deleted"] = include_deleted

    params["limit"] = limit

    params["matter_id"] = matter_id

    json_order: Unset | str = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["page_token"] = page_token

    params["parent_id"] = parent_id

    params["query"] = query

    json_scope: Unset | str = UNSET
    if not isinstance(scope, Unset):
        json_scope = scope.value

    params["scope"] = json_scope

    params["updated_since"] = updated_since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/folders.json",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | FolderList | None:
    if response.status_code == 200:
        response_200 = FolderList.from_dict(response.json())

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
) -> Response[Error | FolderList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    contact_id: Unset | int = UNSET,
    created_since: Unset | str = UNSET,
    document_category_id: Unset | int = UNSET,
    external_property_name: Unset | str = UNSET,
    external_property_value: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    include_deleted: Unset | bool = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    order: Unset | FolderindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    parent_id: Unset | int = UNSET,
    query: Unset | str = UNSET,
    scope: Unset | FolderindexScope = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[Error | FolderList]:
    """Return the data for all Folders

     Outlines the parameters, optional and required, used when requesting the data for all Folders

    Args:
        contact_id (Union[Unset, int]):
        created_since (Union[Unset, str]):
        document_category_id (Union[Unset, int]):
        external_property_name (Union[Unset, str]):
        external_property_value (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        include_deleted (Union[Unset, bool]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, FolderindexOrder]):
        page_token (Union[Unset, str]):
        parent_id (Union[Unset, int]):
        query (Union[Unset, str]):
        scope (Union[Unset, FolderindexScope]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, FolderList]]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        created_since=created_since,
        document_category_id=document_category_id,
        external_property_name=external_property_name,
        external_property_value=external_property_value,
        fields=fields,
        ids=ids,
        include_deleted=include_deleted,
        limit=limit,
        matter_id=matter_id,
        order=order,
        page_token=page_token,
        parent_id=parent_id,
        query=query,
        scope=scope,
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
    contact_id: Unset | int = UNSET,
    created_since: Unset | str = UNSET,
    document_category_id: Unset | int = UNSET,
    external_property_name: Unset | str = UNSET,
    external_property_value: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    include_deleted: Unset | bool = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    order: Unset | FolderindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    parent_id: Unset | int = UNSET,
    query: Unset | str = UNSET,
    scope: Unset | FolderindexScope = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Error | FolderList | None:
    """Return the data for all Folders

     Outlines the parameters, optional and required, used when requesting the data for all Folders

    Args:
        contact_id (Union[Unset, int]):
        created_since (Union[Unset, str]):
        document_category_id (Union[Unset, int]):
        external_property_name (Union[Unset, str]):
        external_property_value (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        include_deleted (Union[Unset, bool]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, FolderindexOrder]):
        page_token (Union[Unset, str]):
        parent_id (Union[Unset, int]):
        query (Union[Unset, str]):
        scope (Union[Unset, FolderindexScope]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, FolderList]
    """

    return sync_detailed(
        client=client,
        contact_id=contact_id,
        created_since=created_since,
        document_category_id=document_category_id,
        external_property_name=external_property_name,
        external_property_value=external_property_value,
        fields=fields,
        ids=ids,
        include_deleted=include_deleted,
        limit=limit,
        matter_id=matter_id,
        order=order,
        page_token=page_token,
        parent_id=parent_id,
        query=query,
        scope=scope,
        updated_since=updated_since,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    contact_id: Unset | int = UNSET,
    created_since: Unset | str = UNSET,
    document_category_id: Unset | int = UNSET,
    external_property_name: Unset | str = UNSET,
    external_property_value: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    include_deleted: Unset | bool = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    order: Unset | FolderindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    parent_id: Unset | int = UNSET,
    query: Unset | str = UNSET,
    scope: Unset | FolderindexScope = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[Error | FolderList]:
    """Return the data for all Folders

     Outlines the parameters, optional and required, used when requesting the data for all Folders

    Args:
        contact_id (Union[Unset, int]):
        created_since (Union[Unset, str]):
        document_category_id (Union[Unset, int]):
        external_property_name (Union[Unset, str]):
        external_property_value (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        include_deleted (Union[Unset, bool]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, FolderindexOrder]):
        page_token (Union[Unset, str]):
        parent_id (Union[Unset, int]):
        query (Union[Unset, str]):
        scope (Union[Unset, FolderindexScope]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, FolderList]]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        created_since=created_since,
        document_category_id=document_category_id,
        external_property_name=external_property_name,
        external_property_value=external_property_value,
        fields=fields,
        ids=ids,
        include_deleted=include_deleted,
        limit=limit,
        matter_id=matter_id,
        order=order,
        page_token=page_token,
        parent_id=parent_id,
        query=query,
        scope=scope,
        updated_since=updated_since,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    contact_id: Unset | int = UNSET,
    created_since: Unset | str = UNSET,
    document_category_id: Unset | int = UNSET,
    external_property_name: Unset | str = UNSET,
    external_property_value: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    include_deleted: Unset | bool = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    order: Unset | FolderindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    parent_id: Unset | int = UNSET,
    query: Unset | str = UNSET,
    scope: Unset | FolderindexScope = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Error | FolderList | None:
    """Return the data for all Folders

     Outlines the parameters, optional and required, used when requesting the data for all Folders

    Args:
        contact_id (Union[Unset, int]):
        created_since (Union[Unset, str]):
        document_category_id (Union[Unset, int]):
        external_property_name (Union[Unset, str]):
        external_property_value (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        include_deleted (Union[Unset, bool]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, FolderindexOrder]):
        page_token (Union[Unset, str]):
        parent_id (Union[Unset, int]):
        query (Union[Unset, str]):
        scope (Union[Unset, FolderindexScope]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, FolderList]
    """

    return (
        await asyncio_detailed(
            client=client,
            contact_id=contact_id,
            created_since=created_since,
            document_category_id=document_category_id,
            external_property_name=external_property_name,
            external_property_value=external_property_value,
            fields=fields,
            ids=ids,
            include_deleted=include_deleted,
            limit=limit,
            matter_id=matter_id,
            order=order,
            page_token=page_token,
            parent_id=parent_id,
            query=query,
            scope=scope,
            updated_since=updated_since,
            x_api_version=x_api_version,
        )
    ).parsed
