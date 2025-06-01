from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.lauk_expense_category_list import LaukExpenseCategoryList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fields: Unset | str = UNSET,
    key: Unset | str = UNSET,
    limit: Unset | int = UNSET,
    name: Unset | str = UNSET,
    page_token: Unset | str = UNSET,
    practice_area: Unset | str = UNSET,
    region: str,
    x_api_version: Unset | str = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["fields"] = fields

    params["key"] = key

    params["limit"] = limit

    params["name"] = name

    params["page_token"] = page_token

    params["practice_area"] = practice_area

    params["region"] = region

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/lauk_expense_categories.json",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | LaukExpenseCategoryList | None:
    if response.status_code == 200:
        response_200 = LaukExpenseCategoryList.from_dict(response.json())

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
) -> Response[Error | LaukExpenseCategoryList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    fields: Unset | str = UNSET,
    key: Unset | str = UNSET,
    limit: Unset | int = UNSET,
    name: Unset | str = UNSET,
    page_token: Unset | str = UNSET,
    practice_area: Unset | str = UNSET,
    region: str,
    x_api_version: Unset | str = UNSET,
) -> Response[Error | LaukExpenseCategoryList]:
    """List Expense Categories

     Outlines the parameters, optional and required, used when requesting the data for all
    LaukExpenseCategories

    Args:
        fields (Union[Unset, str]):
        key (Union[Unset, str]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        page_token (Union[Unset, str]):
        practice_area (Union[Unset, str]):
        region (str):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, LaukExpenseCategoryList]]
    """

    kwargs = _get_kwargs(
        fields=fields,
        key=key,
        limit=limit,
        name=name,
        page_token=page_token,
        practice_area=practice_area,
        region=region,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    fields: Unset | str = UNSET,
    key: Unset | str = UNSET,
    limit: Unset | int = UNSET,
    name: Unset | str = UNSET,
    page_token: Unset | str = UNSET,
    practice_area: Unset | str = UNSET,
    region: str,
    x_api_version: Unset | str = UNSET,
) -> Error | LaukExpenseCategoryList | None:
    """List Expense Categories

     Outlines the parameters, optional and required, used when requesting the data for all
    LaukExpenseCategories

    Args:
        fields (Union[Unset, str]):
        key (Union[Unset, str]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        page_token (Union[Unset, str]):
        practice_area (Union[Unset, str]):
        region (str):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, LaukExpenseCategoryList]
    """

    return sync_detailed(
        client=client,
        fields=fields,
        key=key,
        limit=limit,
        name=name,
        page_token=page_token,
        practice_area=practice_area,
        region=region,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    fields: Unset | str = UNSET,
    key: Unset | str = UNSET,
    limit: Unset | int = UNSET,
    name: Unset | str = UNSET,
    page_token: Unset | str = UNSET,
    practice_area: Unset | str = UNSET,
    region: str,
    x_api_version: Unset | str = UNSET,
) -> Response[Error | LaukExpenseCategoryList]:
    """List Expense Categories

     Outlines the parameters, optional and required, used when requesting the data for all
    LaukExpenseCategories

    Args:
        fields (Union[Unset, str]):
        key (Union[Unset, str]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        page_token (Union[Unset, str]):
        practice_area (Union[Unset, str]):
        region (str):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, LaukExpenseCategoryList]]
    """

    kwargs = _get_kwargs(
        fields=fields,
        key=key,
        limit=limit,
        name=name,
        page_token=page_token,
        practice_area=practice_area,
        region=region,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    fields: Unset | str = UNSET,
    key: Unset | str = UNSET,
    limit: Unset | int = UNSET,
    name: Unset | str = UNSET,
    page_token: Unset | str = UNSET,
    practice_area: Unset | str = UNSET,
    region: str,
    x_api_version: Unset | str = UNSET,
) -> Error | LaukExpenseCategoryList | None:
    """List Expense Categories

     Outlines the parameters, optional and required, used when requesting the data for all
    LaukExpenseCategories

    Args:
        fields (Union[Unset, str]):
        key (Union[Unset, str]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        page_token (Union[Unset, str]):
        practice_area (Union[Unset, str]):
        region (str):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, LaukExpenseCategoryList]
    """

    return (
        await asyncio_detailed(
            client=client,
            fields=fields,
            key=key,
            limit=limit,
            name=name,
            page_token=page_token,
            practice_area=practice_area,
            region=region,
            x_api_version=x_api_version,
        )
    ).parsed
