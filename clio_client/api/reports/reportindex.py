from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.report_list import ReportList
from ...models.reportindex_kind import ReportindexKind
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    category: Unset | str = UNSET,
    created_before: Unset | str = UNSET,
    created_since: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    kind: Unset | ReportindexKind = UNSET,
    limit: Unset | int = UNSET,
    output_format: Unset | str = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    source: Unset | str = UNSET,
    state: Unset | str = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["category"] = category

    params["created_before"] = created_before

    params["created_since"] = created_since

    params["fields"] = fields

    params["ids[]"] = ids

    json_kind: Unset | str = UNSET
    if not isinstance(kind, Unset):
        json_kind = kind.value

    params["kind"] = json_kind

    params["limit"] = limit

    params["output_format"] = output_format

    params["page_token"] = page_token

    params["query"] = query

    params["source"] = source

    params["state"] = state

    params["updated_since"] = updated_since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/reports.json",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ReportList | None:
    if response.status_code == 200:
        response_200 = ReportList.from_dict(response.json())

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
) -> Response[Error | ReportList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    category: Unset | str = UNSET,
    created_before: Unset | str = UNSET,
    created_since: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    kind: Unset | ReportindexKind = UNSET,
    limit: Unset | int = UNSET,
    output_format: Unset | str = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    source: Unset | str = UNSET,
    state: Unset | str = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[Error | ReportList]:
    """Return the data for all Reports

     Outlines the parameters, optional and required, used when requesting the data for all Reports

    Args:
        category (Union[Unset, str]):
        created_before (Union[Unset, str]):
        created_since (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        kind (Union[Unset, ReportindexKind]):
        limit (Union[Unset, int]):
        output_format (Union[Unset, str]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        source (Union[Unset, str]):
        state (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ReportList]]
    """

    kwargs = _get_kwargs(
        category=category,
        created_before=created_before,
        created_since=created_since,
        fields=fields,
        ids=ids,
        kind=kind,
        limit=limit,
        output_format=output_format,
        page_token=page_token,
        query=query,
        source=source,
        state=state,
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
    category: Unset | str = UNSET,
    created_before: Unset | str = UNSET,
    created_since: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    kind: Unset | ReportindexKind = UNSET,
    limit: Unset | int = UNSET,
    output_format: Unset | str = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    source: Unset | str = UNSET,
    state: Unset | str = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Error | ReportList | None:
    """Return the data for all Reports

     Outlines the parameters, optional and required, used when requesting the data for all Reports

    Args:
        category (Union[Unset, str]):
        created_before (Union[Unset, str]):
        created_since (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        kind (Union[Unset, ReportindexKind]):
        limit (Union[Unset, int]):
        output_format (Union[Unset, str]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        source (Union[Unset, str]):
        state (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ReportList]
    """

    return sync_detailed(
        client=client,
        category=category,
        created_before=created_before,
        created_since=created_since,
        fields=fields,
        ids=ids,
        kind=kind,
        limit=limit,
        output_format=output_format,
        page_token=page_token,
        query=query,
        source=source,
        state=state,
        updated_since=updated_since,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    category: Unset | str = UNSET,
    created_before: Unset | str = UNSET,
    created_since: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    kind: Unset | ReportindexKind = UNSET,
    limit: Unset | int = UNSET,
    output_format: Unset | str = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    source: Unset | str = UNSET,
    state: Unset | str = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[Error | ReportList]:
    """Return the data for all Reports

     Outlines the parameters, optional and required, used when requesting the data for all Reports

    Args:
        category (Union[Unset, str]):
        created_before (Union[Unset, str]):
        created_since (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        kind (Union[Unset, ReportindexKind]):
        limit (Union[Unset, int]):
        output_format (Union[Unset, str]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        source (Union[Unset, str]):
        state (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ReportList]]
    """

    kwargs = _get_kwargs(
        category=category,
        created_before=created_before,
        created_since=created_since,
        fields=fields,
        ids=ids,
        kind=kind,
        limit=limit,
        output_format=output_format,
        page_token=page_token,
        query=query,
        source=source,
        state=state,
        updated_since=updated_since,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    category: Unset | str = UNSET,
    created_before: Unset | str = UNSET,
    created_since: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    kind: Unset | ReportindexKind = UNSET,
    limit: Unset | int = UNSET,
    output_format: Unset | str = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    source: Unset | str = UNSET,
    state: Unset | str = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Error | ReportList | None:
    """Return the data for all Reports

     Outlines the parameters, optional and required, used when requesting the data for all Reports

    Args:
        category (Union[Unset, str]):
        created_before (Union[Unset, str]):
        created_since (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        kind (Union[Unset, ReportindexKind]):
        limit (Union[Unset, int]):
        output_format (Union[Unset, str]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        source (Union[Unset, str]):
        state (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ReportList]
    """

    return (
        await asyncio_detailed(
            client=client,
            category=category,
            created_before=created_before,
            created_since=created_since,
            fields=fields,
            ids=ids,
            kind=kind,
            limit=limit,
            output_format=output_format,
            page_token=page_token,
            query=query,
            source=source,
            state=state,
            updated_since=updated_since,
            x_api_version=x_api_version,
        )
    ).parsed
