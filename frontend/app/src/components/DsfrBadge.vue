<script setup lang="ts">
import { reactive } from 'vue'
import { DsfrBadge } from '@gouvminint/vue-dsfr'

import { useStreamlit } from '../streamlit'
import type { ComponentProps } from '../types/ComponentProps'

useStreamlit()

const props = defineProps<
	ComponentProps<{
		small?: boolean
		type?: 'error' | 'success' | 'new' | 'info' | 'warning'
		label?: string
		noIcon?: boolean
		ellipsis?: boolean
	}>
>()

const style = reactive<{ [key: string]: string }>({})

if (props.theme)
{
	style['--base'] = props.theme.base
	style['--primary-color'] = props.theme.primaryColor
	style['--background-color'] = props.theme.backgroundColor
	style['--secondary-background-color'] = props.theme.secondaryBackgroundColor
	style['--text-color'] = props.theme.textColor
	style['--font'] = props.theme.font
}
</script>

<template>
	<div class="component" :style="style">
		<DsfrBadge v-bind="props.args" />
	</div>
</template>
