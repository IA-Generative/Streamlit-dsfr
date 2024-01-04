import type { ComponentProps as StreamlitComponentProps } from '~/stcomponentlib'

interface ComponentProps<ArgType = any> extends StreamlitComponentProps
{
    args: ArgType
}

export type { ComponentProps }
