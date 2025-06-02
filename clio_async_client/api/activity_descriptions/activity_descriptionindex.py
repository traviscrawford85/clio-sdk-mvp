from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_description_list import ActivityDescriptionList
from ...models.activity_descriptionindex_type import ActivityDescriptionindexType
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created_since: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    flat_rate: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    rate_formatter_id: Union[Unset, int] = UNSET,
    rate_foruser_id: Union[Unset, int] = UNSET,
    type_: Union[Unset, ActivityDescriptionindexType] = UNSET,
    updated_since: Union[Unset, str] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["created_since"] = created_since

    params["fields"] = fields

    params["flat_rate"] = flat_rate

    params["ids[]"] = ids

    params["limit"] = limit

    params["page_token"] = page_token

    params["rate_for[matter_id]"] = rate_formatter_id

    params["rate_for[user_id]"] = rate_foruser_id

    json_type_: Union[Unset, str] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["updated_since"] = updated_since

    params["user_id"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/activity_descriptions.json",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ActivityDescriptionList, Error]]:
    if response.status_code == 200:
        response_200 = ActivityDescriptionList.from_dict(response.json())

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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ActivityDescriptionList, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    created_since: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    flat_rate: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    rate_formatter_id: Union[Unset, int] = UNSET,
    rate_foruser_id: Union[Unset, int] = UNSET,
    type_: Union[Unset, ActivityDescriptionindexType] = UNSET,
    updated_since: Union[Unset, str] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[ActivityDescriptionList, Error]]:
    """Return the data for all ActivityDescriptions

     Outlines the parameters, optional and required, used when requesting the data for all
    ActivityDescriptions

    Args:
        created_since (Union[Unset, str]):
        fields (Union[Unset, str]):
        flat_rate (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        page_token (Union[Unset, str]):
        rate_formatter_id (Union[Unset, int]):
        rate_foruser_id (Union[Unset, int]):
        type_ (Union[Unset, ActivityDescriptionindexType]):
        updated_since (Union[Unset, str]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActivityDescriptionList, Error]]
    """

    kwargs = _get_kwargs(
        created_since=created_since,
        fields=fields,
        flat_rate=flat_rate,
        ids=ids,
        limit=limit,
        page_token=page_token,
        rate_formatter_id=rate_formatter_id,
        rate_foruser_id=rate_foruser_id,
        type_=type_,
        updated_since=updated_since,
        user_id=user_id,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    created_since: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    flat_rate: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    rate_formatter_id: Union[Unset, int] = UNSET,
    rate_foruser_id: Union[Unset, int] = UNSET,
    type_: Union[Unset, ActivityDescriptionindexType] = UNSET,
    updated_since: Union[Unset, str] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[ActivityDescriptionList, Error]]:
    """Return the data for all ActivityDescriptions

     Outlines the parameters, optional and required, used when requesting the data for all
    ActivityDescriptions

    Args:
        created_since (Union[Unset, str]):
        fields (Union[Unset, str]):
        flat_rate (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        page_token (Union[Unset, str]):
        rate_formatter_id (Union[Unset, int]):
        rate_foruser_id (Union[Unset, int]):
        type_ (Union[Unset, ActivityDescriptionindexType]):
        updated_since (Union[Unset, str]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ActivityDescriptionList, Error]
    """

    return sync_detailed(
        client=client,
        created_since=created_since,
        fields=fields,
        flat_rate=flat_rate,
        ids=ids,
        limit=limit,
        page_token=page_token,
        rate_formatter_id=rate_formatter_id,
        rate_foruser_id=rate_foruser_id,
        type_=type_,
        updated_since=updated_since,
        user_id=user_id,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    created_since: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    flat_rate: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    rate_formatter_id: Union[Unset, int] = UNSET,
    rate_foruser_id: Union[Unset, int] = UNSET,
    type_: Union[Unset, ActivityDescriptionindexType] = UNSET,
    updated_since: Union[Unset, str] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[ActivityDescriptionList, Error]]:
    """Return the data for all ActivityDescriptions

     Outlines the parameters, optional and required, used when requesting the data for all
    ActivityDescriptions

    Args:
        created_since (Union[Unset, str]):
        fields (Union[Unset, str]):
        flat_rate (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        page_token (Union[Unset, str]):
        rate_formatter_id (Union[Unset, int]):
        rate_foruser_id (Union[Unset, int]):
        type_ (Union[Unset, ActivityDescriptionindexType]):
        updated_since (Union[Unset, str]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActivityDescriptionList, Error]]
    """

    kwargs = _get_kwargs(
        created_since=created_since,
        fields=fields,
        flat_rate=flat_rate,
        ids=ids,
        limit=limit,
        page_token=page_token,
        rate_formatter_id=rate_formatter_id,
        rate_foruser_id=rate_foruser_id,
        type_=type_,
        updated_since=updated_since,
        user_id=user_id,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    created_since: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    flat_rate: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    rate_formatter_id: Union[Unset, int] = UNSET,
    rate_foruser_id: Union[Unset, int] = UNSET,
    type_: Union[Unset, ActivityDescriptionindexType] = UNSET,
    updated_since: Union[Unset, str] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[ActivityDescriptionList, Error]]:
    """Return the data for all ActivityDescriptions

     Outlines the parameters, optional and required, used when requesting the data for all
    ActivityDescriptions

    Args:
        created_since (Union[Unset, str]):
        fields (Union[Unset, str]):
        flat_rate (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        page_token (Union[Unset, str]):
        rate_formatter_id (Union[Unset, int]):
        rate_foruser_id (Union[Unset, int]):
        type_ (Union[Unset, ActivityDescriptionindexType]):
        updated_since (Union[Unset, str]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ActivityDescriptionList, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            created_since=created_since,
            fields=fields,
            flat_rate=flat_rate,
            ids=ids,
            limit=limit,
            page_token=page_token,
            rate_formatter_id=rate_formatter_id,
            rate_foruser_id=rate_foruser_id,
            type_=type_,
            updated_since=updated_since,
            user_id=user_id,
            x_api_version=x_api_version,
        )
    ).parsed
