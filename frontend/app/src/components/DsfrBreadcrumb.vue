<script setup lang="ts">
import { reactive } from 'vue'
import { DsfrBreadcrumb } from '@gouvminint/vue-dsfr'

import { useStreamlit } from '../streamlit'
import type { ComponentProps } from '../types/ComponentProps'

useStreamlit()

const props = defineProps<
	ComponentProps<{
		links?: {
			to: string
			link: string
		}[]
		breadcrumbId?: string
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
		<DsfrBreadcrumb v-bind="props.args" />
	</div>
</template>
