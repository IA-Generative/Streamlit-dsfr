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
			text: string
		}[]
		breadcrumbId?: string
	}>
>()
</script>

<template>
	<div class="component">
		<DsfrBreadcrumb v-bind="props.args" />
	</div>
</template>
